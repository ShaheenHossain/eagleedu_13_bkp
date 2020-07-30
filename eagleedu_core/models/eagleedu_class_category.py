# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduClassCategory(models.Model):
    _name='eagleedu.class_category'
    _description='Class Category list'

    name=fields.Char(string='Class Category')
    code=fields.Char(string='Category code')
    class_category_id = fields.Many2one('eagleedu.class_category', string="Class Category")

