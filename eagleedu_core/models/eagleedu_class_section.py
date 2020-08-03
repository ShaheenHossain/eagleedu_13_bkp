# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSection(models.Model):
    _name = 'eagleedu.class.section'
    _description = "Class Section "
    name = fields.Char(string='Section Name', help="Enter the Name of the Section")
    section_code = fields.Char(string='Section Code', help="Enter the Name of the Section")
    sections_ids = fields.Many2many('eagleedu.class.section', 'eagleedu_class_section_rel', 'sections_ids')
    section_id = fields.Many2one('eagleedu.class.section', help='Enter the name of section')



