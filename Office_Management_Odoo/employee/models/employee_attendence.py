from pyexpat import model
import random
import time
from odoo import fields, models, api
from datetime import datetime, date

class EmployeeAttendance(models.Model):

    _name = "employee.attendance"
    # odoo will create a table in psql of name specified above - . will be converted to _ 
    # table name = office_employee

    _description = "This is model records daily attendance of employees"

    _rec_name = "emp_name_id"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    # these are fields which are custom defined apart from magic fields
    # this is a many to one field here first parameter is comodel name that is to be linked 
    emp_name_id = fields.Many2one(comodel_name="office.employee", string="Employee Id", required=True)

    # today_date = fields.Date("Today Date", default=date.today(), readonly=True)

    check_in_time = fields.Datetime("Check in datetime", default=lambda *a: time.strftime('%Y-%m-%d %H:%M:%S'), readonly=True)

    employee_status = fields.Selection(
        string="Employee Status",
        selection = [('present', 'Present'), ('absent', 'Absent'), ('leave', 'Leave')],
        required=True
    )

    emp_reason = fields.Text(string="Reason")

    age = fields.Char("Employee Age", default="", required=True)

    # onchange fields 

    department = fields.Selection(
        string = 'Department Type',
        selection = [('sales', 'Sales'), ('admin', 'Admin'),('odoo', 'Odoo'), ('oracle', 'Oracle'), 
        ('helper', 'Helper'), ('director', 'Director')],
        help='This is for selection of departments in an office',
        required=True)
    

    gender = fields.Selection(
        string = 'Gender',
        selection = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        required=True)
        
    
    @api.onchange('emp_name_id')
    def _onchange_emp_name_id(self):
        self.age = self.emp_name_id.age
        self.department = self.emp_name_id.department
        self.gender = self.emp_name_id.gender

class EmployeeLeaveApply(models.Model):
    _name = "employee.leave.apply"
    _description = "Employee now can apply for a leave and wait util the leave is granted"
    _rec_name = "emp_name_id"

    emp_name_id = fields.Many2one(
        string='Employee Id',
        comodel_name='office.employee',
    )


    emp_leave_start = fields.Date(string="Leave start date", required=True)

    emp_leave_end = fields.Date(string="Leave end date", required=True)

    leave_reason = fields.Text(
        string='Leave reason',
        required=True
    )
    
    apply_status = fields.Boolean(string="Apply Status", readonly=True)

    is_leave = fields.Boolean(string="", default=True)

    days = fields.Char("Total days", compute="_compute_days")

    def _compute_days(self):
        for rec in self:
            diff = rec.emp_leave_end - rec.emp_leave_start
            rec.days = diff.days
    

class grantLeave(models.Model):
    _name = "employee.grant.leave"
    _description = "grant leave for a employee who has applied it"
    _rec_name = "emp_leave_id"

    emp_leave_id = fields.Many2one(
        string="Employee leave it",
        comodel_name='employee.leave.apply'        
    )
    



