# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduRoomsnumber(models.Model):
    _name = 'eagleedu.roomnumber'
    _description = "Room Number "
    name = fields.Integer(string='Room Number', help="Enter the Room Number of the Class")
    code = fields.Char(string='Code Number', help="Enter the Room Code Number of the Class")

