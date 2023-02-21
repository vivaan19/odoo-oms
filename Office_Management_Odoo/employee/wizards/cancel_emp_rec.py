from odoo import fields, models, api 

class CancelEmpRec(models.TransientModel):
    _name = 'cancel.emp.rec'
    _description = 'Cancel Employee recruitment' 
    _rec_name = "emp_id"

    emp_id = fields.Many2one("employee.join", string="Employee Id")
    
    emp_name = fields.Char("Name", related='emp_id.name')
    
    emp_job_apply = fields.Selection(
        string='Add department', help='This is for selection of departments in an office', 
        related='emp_id.department_id.dept_name', readonly=True
    )

    dept_exp = fields.Selection(
        string="Experience Required in years", related='emp_id.dept_exp', readonly=True)

    # job type
    dept_job_type = fields.Selection(string="Job type", related='emp_id.dept_job_type', readonly=True)


    emp_rem_reason = fields.Text("Application Removal Reason")
    
    # @api.onchange('emp_id')
    # def _onchange_emp_id(self):
    #     self.emp_name = self.emp_id.name  
    
    def cancel_emp_application(self):
        self.env['employee.join'].search([ ('can_id', '=', 'emp_id') ]).unlink()


    
