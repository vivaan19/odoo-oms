from datetime import date
from odoo import fields, models, api


class EmployeeJoin(models.Model):
    # links to emp_join -> apply now 
    # apply now
    _name = "employee.join"
    _description = "Model for candidates to apply for a job"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "can_id"

    name = fields.Char(string="Candidate Name", required=True)

    @api.onchange('name')
    def _onchange_name(self):
        if self.name:
            self.name = self.name.capitalize()  
        else:
            self.name = ""


    can_id = fields.Char(string="Candidate Id")

    # inherit create method when it trigerred record is saving 

    @api.model
    def create(self, values):


        print("-----------employee Create function is executing")    

        values['can_id'] = self.env['ir.sequence'].next_by_code('employee.apply.code')

        print("--------------------------------------->>>>>>>>>>>>>>",type(values['can_id']))

        vals = {'age':values['age'], 'can_id': values['can_id'], 'department_copy': values['department_copy'], 
                'upload_res': values['upload_res'], 'upload_res_name': values['upload_res_name'], 
                'gender':values['gender'], 'name': values['name'], 'b_date': values['b_date']}
        
        print(">>>>>>",vals)

        self.env['candidate.applied'].create(vals)

        result = super(EmployeeJoin, self).create(values)
    
        return result

    def write(self, values):
        res = super(EmployeeJoin, self).write(values)
        
        print("-----------~~~~>>>>>>Write method working values ---", values)

        print("----->>>>>>>>----- candidate id", self.can_id)
        print("----->>>>>>>>----- type candidate id", type(self.can_id))



        # orm method to update the record in candidate review 

        can_review = self.env['candidate.applied'].search([('can_id', '=', self.can_id)]).write(values)

        print("------>>>>>>>>>>>> updated record", can_review)
        
        return res
    
    # def _pass_vals(self):
    #     vals = {
    #         'can_applied':self.can_id
    #     }
    #     self.env['candidate.applied'].create(vals)
    
    # @api.depends('can_id')
    # def _compute_can_id(self):
    #     for record in self:
    #         nam = record.name.strip()

    #         if len(nam) < 2:
    #             record.can_id = f'{nam.upper()[:len(nam)]}000{record.id}'
    #         else:
    #             record.can_id = f'{nam.upper()[:2]}000{record.id}'

    age = fields.Char("Employee Age", default="Not Specified birthdate", tracking=True)
    
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

    # def _compute_age(self):
    #     for emp in self:
    #         today = date.today()
    #         if emp.b_date:
    #             emp.age = today.year - emp.b_date.year
    #         else:
    #             emp.age = "Birthdate not specified"
    
    @api.onchange('b_date')
    def _onchange_b_date(self):
        today = date.today()
        if self.b_date:
            self.age = today.year - self.b_date.year - 1
        else:
            self.age = "Birthdate not specified"

    # onchange fields 

    # department job description
    dept_job_dec = fields.Html("Job Description")

    # years of experience required add string in selection field its mandatory 
    dept_exp = fields.Selection(
        string="Experience Required in years",
        selection=[('zero_to_one', '0-1'), ('two_three', '2-3'), ('three_five', '3-5'),
                   ('more_than_five', '>5')],
    )

    # job type
    dept_job_type = fields.Selection(string="Job type", selection=[('intern', 'Intership'),
    ('full_time', 'Full Time'),
        ('wfh', 'Work from Home')],
    )

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
    
    # , 'gender': self.gender, 'upload_res_name': self.upload_res_name, 
    #             'upload_res': self.upload_res, }


class CandidateApplied(models.Model):

    # links to candidate_review.xml 
    
    # review candidate

    _name = "candidate.applied"
    _description = "This model allows to review candidates"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "can_id"

    can_id = fields.Char(string="Candidate Id")
    name = fields.Char(string="Candidate Name")
    
    b_date = fields.Date(string="Birthdate", tracking=True)


    def _default_res_user(self):
        print("---------~~~~~~~~~~------~~~~~~~@@@@@@@########---> default executing")
        a = self.env['res.users'].search([('name', '=', 'Joel Willis')], limit=1).id
        return a 

    hiring_manager_id = fields.Many2one("res.users", string="Hiring Manager", default=_default_res_user)  

    performance_candidate = fields.Html("Candidate Performance")
        
    selection_status = fields.Selection(
        string="Selection Status",
        selection=[
            ('selected', 'Selected'),
            ('not_selected', 'Not Selected'),
        ],
        required=True,
        tracking=True,
        default='not_selected',
    
        
    )

    priority = fields.Selection(
        [('0', 'Poor'),
         ('1', 'Below Average'),
         ('2', 'Average'),
         ('3', 'Good'),
         ('4', 'Very Good'),
         ('5', 'Excellent')], string="Priority", default='3'
         
    )

    state = fields.Selection(
        [
            ('resume_received', 'Resume Received'),
            ('written_round', 'Written Round'),
            ('technical_interview', 'Technical Interview'),
            ('hr_interview', 'HR Interview'),
            ('not_selected', 'Not Selected'),
            ('onboarding', 'Onboarding')
        ],

        string="Status",
        default="resume_received",
        required=True,
        #

    )

    # onchange fields 
    age = fields.Char(
        "Age", default="Not Specified birthdate", tracking=True)

    department_copy = fields.Selection(
        string='Applying to',
        selection=[('sales', 'Sales'), ('admin', 'Admin'), ('odoo', 'Odoo'), ('oracle', 'Oracle'),
                   ('helper', 'Helper'), ('director', 'Director')],
        
    )

    # related='can_applied.department_copy'

    gender = fields.Selection(
        string='Gender',
        selection=[('male', 'Male'), ('female', 'Female'),
                   ('others', 'Others')],
        required=True,
        tracking=True,
    )

    upload_res = fields.Binary(string="Uploaded Resume", required=True)
    upload_res_name = fields.Char(default="file")
    
    # @api.onchange('can_applied')
    # def _onchange_can_applied(self):
    #     self.age = self.can_applied.age
    #     self.gender = self.can_applied.gender
    #     self.upload_res = self.can_applied.upload_res
    #     self.upload_res_name = self.can_applied.upload_res_name
    
    def emp_status_select(self):
        # return {
        #     'effect': {
        #         'fadeout': 'slow',
        #         'message': 'Candidate Selected !!!',
        #         'type': 'rainbow_man',
        #     }
        # }
        for rec in self:
            rec.state = "onboarding"
            rec.selection_status = "selected"

    def emp_status_not_select(self):
        for rec in self:
            rec.state = "not_selected"
    
    def emp_status_written(self):
        for rec in self:
            rec.state = "written_round"
    
    def emp_status_tech_interview(self):
        for rec in self:
            rec.state = "technical_interview"

    
    def emp_status_hr_interview(self):
        for rec in self:
            rec.state = "hr_interview"
    
    


class DepartmentDesc(models.Model):

    # links to emp_join -> job posting 

    _name = "department.desc"
    _description = "Number of departments in office"
    _rec_name = "job_id"

    # department name to be added
    dept_name = fields.Selection(
        string='Add department',
        selection=[('sales', 'Sales'), ('admin', 'Admin'), ('odoo', 'Odoo'), ('oracle', 'Oracle'),
                   ('helper', 'Helper'), ('director', 'Director')],
        help='This is for selection of departments in an office',
        required=True
        # tracking=True
    )

    job_id = fields.Char("Job Id", compute='_compute_job_id' )
    
    def _compute_job_id(self):
        for rec in self:
            rec.job_id = f'[JOB00{rec.id}] {rec.dept_name.upper()}'

    # @api.onchange('dept_name')
    # def _onchange_dept_name(self):
    #     self.job_id = f'JOB000{str(self.id).replace("NewId_", "")}'

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
    