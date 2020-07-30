from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime

class EagleeduCoreData(models.Model):
    _name='eagleedu.core.data'
    _description='this is education core data for import'
    name=fields.Char("Data Import")
