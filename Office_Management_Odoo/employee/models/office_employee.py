from odoo import fields, models 
from datetime import datetime, date

class OfficeEmployee(models.Model):
    _name = "office.employee"
    # odoo will create a table in psql of name specified above - . will be converted to _ 
    # table name = office_employee

    _description = "This is office employees part of office management system"

    _inherit = ['mail.thread', 'mail.activity.mixin']

    _rec_name = "emp_id"

    # these are fields which are custom defined apart from agic fields

    name = fields.Char("Employee Name", required=True, tracking=True)

    emp_id = fields.Char("Employee Id", compute="_compute_emp_id")

    def _compute_emp_id(self):
        for rec in self:
            rec.emp_id = f'{rec.name.split()[0].upper()}00{rec.id}'


    
    age = fields.Char("Employee Age", compute="_compute_age", default="Not Specified birthdate", tracking=True)

    department = fields.Selection(

        string = 'Department Type',
        selection = [('sales', 'Sales'), ('admin', 'Admin'),('odoo', 'Odoo'), ('oracle', 'Oracle'), 
        ('helper', 'Helper'), ('director', 'Director')],
        help='This is for selection of departments in an office',
        required=True,
        tracking=True
    )

    gender = fields.Selection(
        string = 'Gender',
        selection = [('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        required=True,
        tracking=True
    )

    # add an active field if the record archived active would be false, and unarchive active will be true
    # active is reserved keyword and will add archive and unarchive in actions menu

    active = fields.Boolean(string = 'Active', default=True)

    # date time field for employee birthdate 

    b_date = fields.Date(string = "Birthdate", tracking=True)

    # adding employee image 

    emp_image = fields.Image(string="Image", tracking=True)

    # ---------------------------------------------------------------- relational fields

    employee_more_details = fields.One2many("employee.more.details", 'office_employee_id', string="Employee more details", tracking=True)

    emp_hobby = fields.Many2many("employee.hobby", string="Hobbies")

    def _compute_age(self):
        for emp in self:
            today = date.today()
            if emp.b_date:
                emp.age = today.year - emp.b_date.year
            else:
                emp.age = "Birthdate not specified"
    

    # selection is a list of tuples which have key and value pairs 

class EmployeeMoreDetails(models.Model):

    _name = "employee.more.details"
    _description = "This model will be used as one to many"

    company_name = fields.Char("Company Name", default="BeyonData")

    work_phone = fields.Char(string = "Work Mobile Number")

    work_email = fields.Char("Work Email")

    work_location = fields.Text("Work Location")

    personal_mob = fields.Integer("Personal Mobile Number")

    personal_email = fields.Char("Personal Email")

    office_employee_id = fields.Many2one("office.employee", string="Office Employee M2O")

class EmployeeHobby(models.Model):
    _name = "employee.hobby"
    _description = "for many to many relationship"
    _rec_name = "hobbies"

    hobbies = fields.Char("Hobbies", required=True)