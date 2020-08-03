# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSubject(models.Model):
    _name = 'eagleedu.subject'
    _description = "Subject "
    name = fields.Char(string='Subject Name', help="Enter the Name of the Subject")
    code = fields.Char(string='Subject Code', help="Enter the Code of the Subject")
    subjects_ids = fields.Char(string='Subject Code', help="Enter the Code of the Subject")
    subjects_ids = fields.Many2many('eagleedu.subject', 'eagleedu_subject_rel', 'subjects_ids')


