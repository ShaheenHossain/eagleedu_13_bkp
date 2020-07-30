
from eagle import models, fields, api, _
from eagle.exceptions import UserError, ValidationError


class EagleeduExam(models.Model):
    _name = 'eagleedu.exam'
    _rec_name = "exam_type"

    name = fields.Char(string='Exam Name', default='New')
    # generated_name=fields.Char(string='Gen Name',default='New')
    class_id = fields.Many2one('eagleedu.standard_class', string='Class')
    division_id = fields.Many2one('eagleedu.class.division', string='Division')
    exam_type = fields.Many2one('eagleedu.exam.type', string='Exam Type', required=True)
    # academic_year = fields.Many2one('eagleedu.academic.year', string='Academic Year',
    #                                 related='division_id.academic_year_id', store=True)




class EagleeduExamType(models.Model):
    _name = 'eagleedu.exam.type'

    name = fields.Char(string='Exam Name', required=True)

