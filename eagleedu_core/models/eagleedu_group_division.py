# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduGroupdivision(models.Model):
    _name = 'eagleedu.group_division'
    _description = "Group Division "
    name = fields.Char(string='Group Division', help="Enter the Name of the Group Division")

    group_divisions_ids = fields.Many2many('eagleedu.group_division', 'eagleedu_group_division_rel', 'group_divisions_ids')


