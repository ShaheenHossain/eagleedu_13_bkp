# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduCampus(models.Model):
    _name='eagleedu.campus'
    _inherits={'res.company':'company_id'}
    _description='School Campus of instititution'

    # name=fields.Char(string='Campus Name')
    code=fields.Char(string='Campus code')
    main_campus=fields.Boolean("Main Campus?",default="False")
    parent_campus=fields.Many2one('ealgeedu.campus',"Parent Campus?",default="False")
    shift=fields.Many2many("eagleedu.shift",'eagleedu_campus_shift_rel','shift','campus',string='Shifts')

class EagleeduShift(models.Model):
    _name='eagleedu.shift'
    _description='Shifts in the School Campus'

    name=fields.Char(string='Shift Name')
    code=fields.Char(string='shift code')
    campus =fields.Many2many("eagleedu.campus",'eagleedu_campus_shift_rel','campus','shift',string='Shifts')