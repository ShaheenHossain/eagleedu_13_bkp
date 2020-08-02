# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduGuardianRelation(models.Model):
    _name = 'eagleedu.guardian.relation'
    _description = 'This the Guardian'
    name = fields.Char()
    gender=fields.Selection([('male',"Male"), ('female','Female')])
    relation=fields.Char(string='Relation', required=False)
    reverse_male=fields.Char(string='Reverse  Relation (Male)',required=False)
    reverse_female=fields.Char(string='Reverse Relation (Female)',required=False)