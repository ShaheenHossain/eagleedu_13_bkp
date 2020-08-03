# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _



class EagleeduClassHistory(models.Model):
    _name = 'eagleedu.class.history'
    _description = "Student Class history"
    _rec_name = 'class_id'

    academic_year_id = fields.Many2one('eagleedu.academic.year', string='Academic Year', help="Select the Academic Year")
    class_id = fields.Many2one('eagleedu.class.division', string='Class', help="Select the class")
    level=fields.Many2one('eagleedu.class',string='level',related='class_id.class_id',store=True) #related='class_id.class_id'
    section=fields.Many2one('eagleedu.class.section',string='section',related='class_id.section_id') #
    from_date=fields.Date('From')
    till_date=fields.Date('Till')
    student_id = fields.Many2one('eagleedu.student', string='Students')
    adm_no=fields.Char(string="Student ID", related='student_id.adm_no')
    roll_no=fields.Integer('Roll No',required=True)
    compulsory_subjects=fields.Many2many('eagleedu.syllabus','eagleedu_syllabus_class_history_rel',
                                         'compulsory_subjects','compulsory_for',string='Compulsory')
    selective_subjects=fields.Many2many('eagleedu.syllabus','eagleedu_syllabus_class_history_1_rel',
                                        'selective_subjects','selective_for',string='Selective')
    optional_subjects=fields.Many2many('eagleedu.syllabus','eagleedu_syllabus_class_history_optional_rel',
                                        'optional_subjects','optional_for',string='Optional')
    # selective_subjects=fields.Many2many('eagleedu.syllabus','selective_for',string='Selective')
    # optional_subjects=fields.Many2many('eagleedu.syllabus','optional_for',string='Optional')
    _sql_constraints = [
        ('student_class_history', 'unique(academic_year_id,student_id)', "Student mustbe Unique for a year"),
        ('student_class_history', 'unique(academic_year_id,class_id,roll_no)', "Roll no must be qnique for Class"),
    ]