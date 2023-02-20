from odoo import fields, models, api 

class CancelEmpRec(models.TransientModel):
    _name = 'cancel.emp.rec'
    _description = 'Cancel Employee recruitment' 
    _rec_name = "emp_id"

    emp_id = fields.Many2one("candidate.applied", string="Employee Id")
    emp_name = fields.Char("Name")
    emp_rem_reason = fields.Text("Application Removal Reason")
    
    @api.onchange('emp_id')
    def _onchange_emp_id(self):
        self.emp_name = self.emp_id.can_applied.name


    
