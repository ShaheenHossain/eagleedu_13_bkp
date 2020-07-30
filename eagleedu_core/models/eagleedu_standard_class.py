# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduClass(models.Model):
    _name = 'eagleedu.standard_class'
    _description = "Class Standard Level"
    sequence=fields.Integer("Sequence")
    name = fields.Char(string='Class', required=True, help="Enter the Name of the Class")
    standard_class_id = fields.Many2one('eagleedu.standard_class', string='Class', help="Enter the Name of the Class")

    class_section_id = fields.Many2one('eagleedu.class_section', string='Section Name', help="Enter the Name of the Section")
    class_sections_ids = fields.Many2many('eagleedu.class_section', string='Sections Names', help="Enter the Name of the Section")
    roman_name = fields.Char(string='Roman Name ', help="Enter the Code of the Class")

    group_division_id = fields.Many2one('eagleedu.group_division', string='Group Division', help="Enter the Name of the Group division")
    group_division_ids = fields.Many2many('eagleedu.group_division', string='Groups Divisions', help="Enter the Name of the Group division")
    subjects_ids = fields.Many2many('eagleedu.subject', string='Subjects Names ', help="Enter the Name of the Group division")
    class_category_id = fields.Many2one('eagleedu.class_category', string='Class Category', help="Enter the Name of the Class Category")

