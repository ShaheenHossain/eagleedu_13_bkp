# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _


class EagleeduRoomname(models.Model):
    _name = 'eagleedu.roomname'
    _description = "Room Name "
    name = fields.Char(string='Room Name', help="Enter the Room Name of the Class")
    code = fields.Char(string='Room Code', help="Enter the Room Code of the Class")


