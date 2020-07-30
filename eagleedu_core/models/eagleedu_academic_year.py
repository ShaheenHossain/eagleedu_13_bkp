from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
from datetime import datetime,date
from calendar import monthrange

class EagleeduAcademicYear(models.Model):
    _name = 'eagleedu.academic.year'
    _description = 'Academic Year'
    _order = 'sequence asc'
    _rec_name = 'name'

    name = fields.Char(string='Year Name', required=True, help='Name of academic year')
    ay_code = fields.Char(string='Code', compute='set_ay_code', required=True,
                              help='Code of academic year')  # related='name',
    sequence = fields.Integer(string='Sequence', required=True)
    ay_description = fields.Text(string='Description', help="Description about the academic year")
    active = fields.Boolean('Active', default=True,
                            help="If unchecked, it will allow you to hide the Academic Year without removing it.")

    current_year = datetime.now().year

    start_date = fields.Datetime(string='Start Date', default=datetime.strptime('%s-01-01' % (current_year), '%Y-%m-%d'))
    end_date = fields.Datetime(string='End Date', default=datetime.strptime('%s-12-31' % (current_year), '%Y-%m-%d'))

    ay_id = fields.Many2one('eagleedu.academic.year', string='Year ID', help='Name of academic year')

    @api.model
    def create(self, vals):
        """Over riding the create method and assigning the
        sequence for the newly creating record"""
        vals['sequence'] = self.env['ir.sequence'].next_by_code('eagleedu.academic.year')
        res = super(EagleeduAcademicYear, self).create(vals)
        return res


    @api.onchange('name')
    def set_ay_code(self):
        self.ay_code = self.name