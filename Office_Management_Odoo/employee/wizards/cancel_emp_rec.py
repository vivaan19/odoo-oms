from odoo import fields, models, api 

class CancelEmpRec(models.TransientModel):
    _name = 'cancel.emp.rec'
    _description = 'Cancel Employee recruitment' 
    _rec_name = "emp_id"

    emp_id = fields.Many2one("employee.join", string="Employee Id")
    
    emp_name = fields.Char("Name", related='emp_id.name')
    
    emp_job_apply = fields.Many2one("", related='emp_id.department_id')

    emp_rem_reason = fields.Text("Application Removal Reason")
    
    # @api.onchange('emp_id')
    # def _onchange_emp_id(self):
    #     self.emp_name = self.emp_id.name  
    
    def cancel_emp_application(self):
        self.env['employee.join'].search([ ('can_id', '=', 'emp_id') ]).unlink()


    
