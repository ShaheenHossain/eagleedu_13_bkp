# -*- coding: utf-8 -*-

from eagle.exceptions import ValidationError
from eagle import fields, models, api, _

class EagleeduClassDivision(models.Model):
    _name = 'eagleedu.class.division'
    _description = "Class room"


    name = fields.Char(string='Name')
    display=fields.Char('Class Name')
    room_id=fields.Many2one('eagleedu.roomname', string="Room Name")
    roomnong_id=fields.Many2one('eagleedu.roomnumber', string="Room Number")
    # roomname_id=fields.Many2one('eagleedu.roomname')
    actual_strength = fields.Integer(string='Max student No', default=60, help="Total strength of the class")
    instructor_id = fields.Many2one('eagleedu.instructor', string='Class Teacher', help="Class teacher/Faculty")
    # class_division_id = fields.Char('eagleedu.class.division', string='Class Division', help="Class Division")
    academic_year_id = fields.Many2one('eagleedu.academic.year', string='Academic Year',
                                       help="Select the Academic Year", required=True)
    class_id = fields.Many2one('eagleedu.class', string='Class', required=True,
                               help="Select the Class")
    division_id = fields.Many2one('eagleedu.group_division', string='Group Division',help="Select the Division")
    section_id = fields.Many2one('eagleedu.class.section', string='Section', help="Select the Section")
    students_ids = fields.One2many('eagleedu.student', 'class_id', string='Students')
    # student_count = fields.Integer(string='Students Count', compute='_get_student_count')
    # class_room=fields.Many2one('education.rooms','Room No')

    @api.model
    def create(self, vals):
        """Return the name as a str of class + division"""
        #res = super(EagleeduClassDivision, self).create(vals)
        class_id = self.env['eagleedu.class'].browse(vals['class_id'])
        division_id = self.env['eagleedu.group_division'].browse(vals['division_id'])
        section_id = self.env['eagleedu.class.section'].browse(vals['section_id'])
        batch = self.env['eagleedu.academic.year'].browse(vals['academic_year_id'])
        # room_id = self.env['eagleedu.roomname'].browse(vals['room_id'])
        # roomnong_id = self.env['eagleedu.roomnumber'].browse(vals['roomnong_id'])
        className=''
        divisionName=''
        sectionName=''
        batchName=batch.ay_code
        # roomName=''
        # roomnongName=''
        if class_id.id>0:
            className=class_id.name
        if division_id.id>0:
            divisionName=division_id.name
        if section_id.id>0:
            sectionName=section_id.name
        # if room_id.id>0:
        #     roomName=room_id.name
        # if roomnong_id.id>0:
        #     roomnongName=roomnong_id.name

        name = str(className + '-' + divisionName+ '-' + sectionName+ '-' + batchName) #+ '-'+ roomName+ '-' + roomnongName
        vals['name'] = name
        #
        # name = str(className+ '-'+ divisionName+ '-' + sectionName+ '-' + batchName+ '-'+ roomName+ '-' + roomnongName)
        # vals['display'] = name

        return super(EagleeduClassDivision, self).create(vals)


#    @api.multi
    # def view_students(self):
    #     """Return the list of current students in this class"""
    #     self.ensure_one()
    #     students = self.env['eagleedu.student'].search([('class_id', '=', self.id)])
    #     students_list = students.mapped('id')
    #     return {
    #         'domain': [('id', 'in', students_list)],
    #         'name': _('Students'),
    #         'view_mode': 'form',
    #         'view_mode': 'tree,form',
    #         'res_model': 'eagleedu.student',
    #         'view_id': False,
    #         'context': {'default_class_id': self.id},
    #         'type': 'ir.actions.act_window'
    #     }

    # def _get_student_count(self):
    #     """Return the number of students in the class"""
    #     for rec in self:
    #         students = self.env['eagleedu.student'].search([('class_id', '=', rec.id)])
    #         student_count = len(students) if students else 0
    #         rec.update({
    #             'student_count': student_count
    #         })

    @api.constrains('actual_strength')
    def validate_strength(self):
        """Return Validation error if the students strength is not a non-zero number"""
        for rec in self:
            if rec.actual_strength <= 0:
                raise ValidationError(_('Max Student No must be greater than Zero'))

    _sql_constraints=[
        ('ad_no', 'unique(name)', "class should be unique!"),
    ]

