# -*- coding: utf-8 -*-


from eagle import fields, models, api, _
from eagle.exceptions import ValidationError

from datetime import datetime

class EagleeduAssigningClass(models.Model):
    _name = 'eagleedu.assigning.class'
    _description = 'Assign the Students to Class'
    _inherit = ['mail.thread']
    # _rec_name = 'class_assign_name'
    name = fields.Char('Class Assign Register', compute='get_class_assign_name')
    keep_roll_no=fields.Boolean("keep Roll No")
    class_id = fields.Many2one('eagleedu.class', string='Class')
    student_list = fields.One2many('eagleedu.student.list', 'connect_id', string="Students")
    admitted_class = fields.Many2one('eagleedu.class.division', string="Admitted Class" )
    assigned_by = fields.Many2one('res.users', string='Assigned By', default=lambda self: self.env.uid)
    state = fields.Selection([('draft', 'Draft'), ('done', 'Done')],
                             string='State', required=True, default='draft', track_visibility='onchange')


    assign_date = fields.Datetime(string='Asigned Date', default=datetime.today())

    #assign_date = fields.Date(string='Assigned Date',default=fields.date.today())


    @api.model
    def get_class_assign_name(self):
        for rec in self:
            rec.name = str(rec.admitted_class.name) + '(Assign on ' + str(rec.assign_date) +')'
            #rec.name = rec.admitted_class.name #+ '(assigned on '+ rec.assign_date +')'



    def assigning_class(self):
        max_roll = self.env['eagleedu.class.history'].search([('class_id','=',self.admitted_class.id)], order='roll_no desc', limit=1)
        if max_roll.roll_no:
            next_roll = max_roll.roll_no
        else:
            next_roll = 0

        for rec in self:

            if not self.student_list:
                raise ValidationError(_('No Student Lines'))
            com_sub = self.env['eagleedu.syllabus'].search(
                            [('class_id', '=', rec.class_id.id),
                             ('academic_year', '=', rec.admitted_class.academic_year_id.id),
                             ('divisional','=',False),
                             ('selection_type', '=', 'compulsory')])
            elect_sub=self.env['eagleedu.syllabus'].search(
                            [('class_id', '=', rec.class_id.id),
                             ('academic_year', '=', rec.admitted_class.academic_year_id.id),
                             ('divisional','=',True),
                             ('division_id','=',rec.admitted_class.id),
                             ('selection_type', '=', 'compulsory')])
            com_subjects = [] # compulsory Subject List
            el_subjects = [] # Elective Subject List
            for sub in com_sub:
                com_subjects.append(sub.id)
            for sub in elect_sub:
                el_subjects.append(sub.id)
            for line in self.student_list:
                st=self.env['eagleedu.student'].search([('id','=',line.student_id.id)])
                st.class_id = rec.admitted_class.id
                if self.keep_roll_no != True:
                    next_roll = next_roll + 1
                    line.roll_no=next_roll
                st.roll_no = line.roll_no


                # create student history

                self.env['eagleedu.class.history'].create({'academic_year_id': rec.admitted_class.academic_year_id.id,
                                                            'class_id': rec.admitted_class.id,
                                                            'student_id': line.student_id.id,
                                                            'roll_no': line.roll_no,
                                                            'compulsory_subjects': [(6, 0,com_subjects)],
                                                            'selective_subjects': [(6, 0, el_subjects)]
                                                            })


            self.write({
                'state': 'done'
                })


    def unlink(self):
        """Return warning if the Record is in done state"""
        for rec in self:
            if rec.state == 'done':
                raise ValidationError(_("Cannot delete Record in Done state"))

    def get_student_list(self):
        """returns the list of students applied to join the selected class"""
        for rec in self:
            for line in rec.student_list:
                line.unlink()
            # TODO apply filter not to get student assigned previously
            students = self.env['eagleedu.student'].search([
                ('class_id', '=', rec.admitted_class.id),('assigned', '=', False)])
            if not students:
                raise ValidationError(_('No Students Available.. !'))
            values = []
            for stud in students:
                stud_line = {
                    'class_id': rec.class_id.id,
                    'student_id': stud.id,
                    'connect_id': rec.id,
                    'roll_no': stud.application_id.roll_no
                }
                stud.assigned=True
                values.append(stud_line)
            for line in values:
                rec.student_line = self.env['eagleedu.student.list'].create(line)


class EagleeduStudentList(models.Model):
    _name = 'eagleedu.student.list'
    _description = 'Eagleedu Student List'
    # _inherit = ['mail.thread']

    connect_id = fields.Many2one('eagleedu.assigning.class', string='Class')
    student_id = fields.Many2one('eagleedu.student', string='Students Name')
    # stu_id=fields.Char(string="Id",related='student_id.student_id')
    adm_no=fields.Char(string="Student ID", related='student_id.adm_no')
    class_id = fields.Many2one('eagleedu.class', string='Level')
    section_id = fields.Many2one('eagleedu.class.section', string='Class')
    roll_no = fields.Integer( string='Roll No')

    # @api.onchange('name')
    # def set_ay_code(self):
    #     self.ay_code = self.name