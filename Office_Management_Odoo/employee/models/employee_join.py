from datetime import date
from odoo import fields, models     

class EmployeeJoin(models.Model):
    _name = "employee.join"
    _description = "this model is for employee recruitment"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Candidate Name", required=True)

    age = fields.Char("Employee Age", compute="_compute_age", default="Not Specified birthdate", tracking=True)

    department = fields.Selection(
        string = 'Applying to',
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

    upload_res = fields.Binary(string="Upload Resume", required=True)
    upload_res_name = fields.Char()

    def _compute_age(self):
        for emp in self:
            today = date.today()
            if emp.b_date:
                emp.age = today.year - emp.b_date.year
            else:
                emp.age = "Birthdate not specified"
    
    


    