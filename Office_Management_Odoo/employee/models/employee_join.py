from datetime import date
from odoo import fields, models, api


class EmployeeJoin(models.Model):
    # links to emp_join -> apply now 
    # apply now
    _name = "employee.join"
    _description = "Model for candidates to apply for a job"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string="Candidate Name", required=True)

    age = fields.Char("Employee Age", compute="_compute_age",
                      default="Not Specified birthdate", tracking=True)
    
    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'),
                   ('others', 'Others')],
        required=True,
        tracking=True
    )

    

    # add an active field if the record archived active would be false, and unarchive active will be true
    # active is reserved keyword and will add archive and unarchive in actions menu

    active = fields.Boolean(string='Active', default=True)

    # date time field for employee birthdate

    b_date = fields.Date(string="Birthdate", tracking=True)

    upload_res = fields.Binary(string="Upload Resume", required=True)
    upload_res_name = fields.Char()

    def _compute_age(self):
        for emp in self:
            today = date.today()
            if emp.b_date:
                emp.age = today.year - emp.b_date.year
            else:
                emp.age = "Birthdate not specified"
    

    # onchange fields 

    # department job description
    dept_job_dec = fields.Html("Job Description", required=True)

    # years of experience required add string in selection field its mandatory 
    dept_exp = fields.Selection(
        string="Experience Required in years",
        selection=[('zero_to_one', '0-1'), ('two_three', '2-3'), ('three_five', '3-5'),
                   ('more_than_five', '>5')],
        required=True)

    # job type
    dept_job_type = fields.Selection(string="Job type", selection=[('intern', 'Intership'),
    ('full_time', 'Full Time'),
        ('wfh', 'Work from Home')],
        required=True)

    department_id = fields.Many2one(
        string='Applying to',
        comodel_name='department.desc',  
    )
    
    department_copy = fields.Selection(
        string='Add department',
        selection=[('sales', 'Sales'), ('admin', 'Admin'), ('odoo', 'Odoo'), ('oracle', 'Oracle'),
                   ('helper', 'Helper'), ('director', 'Director')],
        help='This is for selection of departments in an office',
        required=True
        # tracking=True
    )


    @api.onchange('department_id')
    def _onchange_department_id(self):
        self.dept_job_dec = self.department_id.dept_job_dec
        self.dept_exp = self.department_id.dept_exp
        self.dept_job_type = self.department_id.dept_job_type
        self.department_copy = self.department_id.dept_name


class CandidateApplied(models.Model):

    # links to candidate_review.xml 
    
    # review candidate

    _name = "candidate.applied"
    _description = "This model allows to review candidates"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "can_applied"

    can_applied = fields.Many2one("employee.join", string="Name")

        
    selection_status = fields.Selection(
        string="Selection Status",
        selection=[
            ('selected', 'Selected'),
            ('not_selected', 'Not Selected'),
        ],
        required=True,
        tracking=True
    )

    priority = fields.Selection(
        [('0', 'Poor'),
         ('1', 'Below Average'),
         ('2', 'Average'),
         ('3', 'Good'),
         ('4', 'Very Good'),
         ('5', 'Excellent')], string="Priority"
    )

    state = fields.Selection(
        [
            ('resume_recieved', 'Resume Recieved'),
            ('wrritten_round', 'Wrritten Round'),
            ('technical_interview', 'Technical Interview'),
            ('hr_interview', 'HR Interview'),
            ('not_selected', 'Not Selected'),
            ('onboarding', 'Onboarding')
        ],

        string="Status",
        default="resume_recieved",
        required=True
    )

    # onchange fields 
    age = fields.Char(
        "Age", default="Not Specified birthdate", tracking=True)

    department = fields.Selection(
        string='Applying to',
        selection=[('sales', 'Sales'), ('admin', 'Admin'), ('odoo', 'Odoo'), ('oracle', 'Oracle'),
                   ('helper', 'Helper'), ('director', 'Director')],
        related='can_applied.department_copy'
    )

    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'),
                   ('others', 'Others')],
        required=True,
        tracking=True
    )

    upload_res = fields.Binary(string="Uploaded Resume", required=True)
    upload_res_name = fields.Char(default="file")

    def emp_status_select(self):
        return {
            'effect': {
                'fadeout': 'slow',
                'message': 'Candidate Selected !!!',
                'type': 'rainbow_man',
            }
        }

    def emp_status_not_select(self):
        pass

    @api.onchange('can_applied')
    def _onchange_can_applied(self):
        self.age = self.can_applied.age
        self.gender = self.can_applied.gender
        self.upload_res = self.can_applied.upload_res
        self.upload_res_name = self.can_applied.upload_res_name


class DepartmentDesc(models.Model):

    # links to emp_join -> job posting 

    _name = "department.desc"
    _description = "Number of departments in office"
    _rec_name = "dept_name"

    # department name to be added
    dept_name = fields.Selection(
        string='Add department',
        selection=[('sales', 'Sales'), ('admin', 'Admin'), ('odoo', 'Odoo'), ('oracle', 'Oracle'),
                   ('helper', 'Helper'), ('director', 'Director')],
        help='This is for selection of departments in an office',
        required=True
        # tracking=True
    )

    # department job description
    dept_job_dec = fields.Html("Job Description", required=True)

    # years of experience required add string in selection field its mandatory 
    dept_exp = fields.Selection(
        string="Experience Required in years",
        selection=[('zero_to_one', '0-1'), ('two_three', '2-3'), ('three_five', '3-5'),
                   ('more_than_five', '>5')],
        required=True)

    # job type
    dept_job_type = fields.Selection(string="Job type", selection=[('intern', 'Intership'),
    ('full_time', 'Full Time'),
    ('wfh', 'Work from Home')],
        required=True)
    