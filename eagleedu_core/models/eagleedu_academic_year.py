from eagle import fields, models, api, _
from eagle.exceptions import ValidationError
# from datetime import datetime timedelta
from calendar import monthrange

from datetime import datetime, timedelta

_defaults={
          'date_start': lambda *a:datetime.now().strftime('%Y-%m-%d'),
          'date_end': lambda *a:(datetime.now() + timedelta(days=(6))).strftime('%Y-%m-%d'),
}



# class AcademyRoomNo(models.Model):
#     _name='education.rooms'
#     name=fields.Char('Room Name')
#     code=fields.Integer('Room No')
#     capacity=fields.Integer('Capacity')
#     amenities_ids = fields.One2many('education.class.amenities', 'room_id', string='Amenities')

class EagleeduAcademicYear(models.Model):
    _name = 'eagleedu.academic.year'
    _description = 'Academic Year'
    _order = 'sequence asc'
    _rec_name = 'name'

    name = fields.Char(string='Year Name', required=True, help='Name of academic year')
    # academic_year_id = fields.Char(string='Year Name', required=True, help='Name of academic year')
    ay_code = fields.Char(string='Code', compute='set_ay_code', required=True, help='Code of academic year') # related='name',
    sequence = fields.Integer(string='Sequence', required=True)

    current_year = datetime.now().year

    start_date = fields.Datetime(string='Start Date', default=datetime.strptime('%s-01-01' % (current_year), '%Y-%m-%d'))
    end_date = fields.Datetime(string='End Date', default=datetime.strptime('%s-12-31' % (current_year), '%Y-%m-%d'))


    # academic_year_start_date = fields.Date(string='Start date', required=True, help='Starting date of academic year')
    # academic_year_end_date = fields.Date(string='End date', required=True, help='Ending of academic year')

    # start_date = fields.Date(string='Start date', required=True, help='Starting date of academic year')
    # end_date = fields.Date(string='End date', required=True, help='Ending of academic year')

    # start_date = fields.Date(string='Start Date', required=True, default=datetime.date.strftime('%Y-01-01'))

    # starting_day_of_current_year = datetime.now().date().replace(month=1, day=1)
    # ending_day_of_current_year = datetime.now().date().replace(month=12, day=31)

    # start_date = fields.Date(string='Start date', required=True, default=time.strftime('%Y-01-01'))
    # end_date = fields.Date(string='End date', required=True, default=time.strftime('%Y-31-12'))

    # date_to = fields.Date(string="End Date", default=time.strftime('%Y-01-01'))


    academic_year_description = fields.Text(string='Description', help="Description about the academic year")
    active = fields.Boolean('Active', default=True,
                            help="If unchecked, it will allow you to hide the Academic Year without removing it.")


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

    #field_2 = fields.Char(string='Test', related='field_1')

    # @api.onchange('academic_year_id')
    # def set_ay_code(self):
    #     if self.academic_year_id:
    #         self.ay_code = self.academic_year_id.name