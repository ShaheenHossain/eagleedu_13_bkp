# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSyllabus(models.Model):
    _name = 'eagleedu.syllabus'
    _description = "Syllabus "
    _rec_name='display'

    name = fields.Char(string='Name', help="Enter the Name of the Syllabus")
    code = fields.Char('Code', compute="_get_code")

    has_group=fields.Integer(string='Has Group')
    divisional=fields.Boolean("Grouping ?")
    class_division_id = fields.Many2one('eagleedu.class.division', string='Group')
    display=fields.Char('Syllabus Display',help="This is printed on the marksheet as Subject")
    class_id = fields.Many2one('eagleedu.standard_class', string='Class ID')
    subject_id = fields.Many2one('eagleedu.subject', string='Subject')
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year')
    paper = fields.Char( string='Paper')
    active=fields.Boolean('Active?',related='academic_year.active')

    subject_type = fields.Selection(
        [('theory', 'Theory'), ('practical', 'Practical'),
         ('both', 'Both'), ('other', 'Other')],
        'Subject Type', default="theory", required=True)
    selection_type = fields.Selection(
        [('compulsory', 'Compulsory'), ('elective', 'Elective')],
        'Selection Type', default="compulsory", required=True)
    evaluation_type = fields.Selection(
        [('general', 'General'),('extra','Extra')],
        'Evaluation Type', default="general", required=True)

    # total_hours = fields.Float(string='Total Hours')
    total_mark=fields.Integer('Total')
    pass_mark=fields.Integer('Pass')
    tut_mark=fields.Integer('Tutorial')
    tut_pass=fields.Integer('pass')
    subj_mark = fields.Integer('Subjective')
    subj_pass = fields.Integer('pass')
    obj_mark = fields.Integer('Objective')
    obj_pass = fields.Integer('pass')
    prac_mark = fields.Integer('Practical')
    prac_pass = fields.Integer('pass')
    description = fields.Text(string='Syllabus Modules')

    compulsory_for = fields.Many2many('eagleedu.class.history', 'eagleedu_syllabus_class_history_rel',
                                      'compulsory_for', 'compulsory_subjects', 'compulsory for')
    selective_for = fields.Many2many('eagleedu.class.history', 'eagleedu_syllabus_class_history_1_rel',
                                     'selective_for', 'selective_subjects', 'selective for')
    optional_for = fields.Many2many('eagleedu.class.history', 'eagleedu_syllabus_class_history_optional_rel',
                                    'optional_for', 'optional_subjects', 'Optional for')

    @api.onchange('academic_year','class_id','class_division_id','subject_id','paper')
    def _get_code(self):
        for rec in self:
            recname=''
            reccode=''
            if rec.paper and rec.subject_id:
                recname=rec.subject_id.name +'-'+ rec.paper
                reccode=rec.subject_id.code +'-'+ rec.paper
            elif rec.subject_id:
                recname=rec.subject_id.name
                reccode=rec.subject_id.code
            rec.display = recname
            if recname != '':
                if  rec.class_id :
                    if rec.academic_year :
                        if rec.divisional == True:
                            recname=recname + rec.class_id.name +'-' + rec.academic_year.name # +' ('+rec.class_division_id.name +')'
                            reccode=reccode + rec.class_id.code +'-' + rec.academic_year.ay_code # +' ('+rec.class_division_id.code +')'
                        else:
                            recname = recname + rec.class_id.name + '-' + rec.academic_year.name
                            reccode = reccode + rec.class_id.code + '-' + rec.academic_year.ay_code
                            rec.class_division_id=False
            rec.name=recname
            rec.code=reccode
    @api.model
    @api.onchange('tut_mark','subj_mark','obj_mark','prac_mark','tut_pass','subj_pass','obj_pass','prac_pass')
    def calculate_total_mark(self):
        for rec in self:
            rec.total_mark=rec.tut_mark+rec.subj_mark+rec.obj_mark+rec.prac_mark
            rec.pass_mark=rec.tut_pass+rec.subj_pass+rec.obj_pass+rec.prac_pass
    _sql_constraints = [('unque_syllabus_batch_level','unique(subject_id,academic_year,class_division_id,class_id,paper)','Subject Already added!'),]