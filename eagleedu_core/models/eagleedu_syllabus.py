# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSyllabus(models.Model):
    _name = 'eagleedu.syllabus'
    _description = "Syllabus "
    _rec_name='syllabus_display'

    name = fields.Char(string='Name', help="Enter the Name of the Syllabus")
    # syllabus_code = fields.Char(string='Syllabus Code', compute="_get_code")
    syllabus_display=fields.Char('Syllabus Display',help="This is printed on the marksheet as Subject")
    standard_class_id = fields.Many2one('eagleedu.standard_class', string='Class ID')
    subject_id = fields.Many2one('eagleedu.subject', string='Subject')
    academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year')

