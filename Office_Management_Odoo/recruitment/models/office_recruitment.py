from odoo import fields, models 

class OfficeEmployee(models.Model):
    _name = "office.employee"
    # odoo will create a table in psql of name specified above - . will be converted to _ 
    # table name = office_employee

    _description = "This is office employees part of office management system"

    # these are fields which are custom defined apart from magic fields

    name = fields.Char("Employee Name", required=True)
    
    age = fields.Integer("Employee Age", required=True)
    
    department = fields.Selection(
        string = 'Type',
        selection = [('sales', 'Sales'), ('admin', 'Admin'),('odoo', 'Odoo'), ('oracle', 'Oracle')],
        help='This is for selection of departments in an office'
    )

    # selection is a list of tuples which have key and value pairs 


    
