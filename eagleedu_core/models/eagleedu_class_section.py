# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduSection(models.Model):
    _name = 'eagleedu.class_section'
    _description = "Class Section "
    name = fields.Char(string='Section Name', help="Enter the Name of the Section")
    class_section_code = fields.Char(string='Section Code', help="Enter the Name of the Section")
    class_sections_ids = fields.Many2many('eagleedu.class_section', 'eagleedu_class_section_rel', 'class_sections_ids')
    class_section_id = fields.Many2one('eagleedu.class_section', help='Enter the name of section')



