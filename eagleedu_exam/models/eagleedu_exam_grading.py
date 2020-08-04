# -*- coding: utf-8 -*-


from eagle import models, fields, api, _

class EagleeduExamGrading(models.Model):
    _name = 'eagleedu.exam.grading'
    _rec_name = 'result'

    min_per = fields.Integer('Minimum Percentage', required=True)
    max_per = fields.Integer('Maximum Percentage', required=True)
    result = fields.Char('Result to Display', required=True)
    score = fields.Float('Score')

    # @api.multi
    def get_grade_point(self,ful_mark,obtained):
        if ful_mark==0:
            ful_mark=1      #####trick to avoide divided by zero error
        obt_per=(obtained/ful_mark)*100
        grading = self.env['eagleedu.exam.grading'].search([('min_per','<=',obt_per)], order='min_per desc',limit=1)
        return grading.score

    # @api.multi
    def get_letter_grade(self,ful_mark,obtained):
        if ful_mark==0:
            ful_mark=1      #####trick to avoide divided by zero error
        obt_per=(obtained/ful_mark)*100
        grading = self.env['eagleedu.exam.grading'].search([('min_per','<=',obt_per)], order='min_per desc',limit=1)
        return grading.result

    # @api.multi
    def get_lg(self,gp):
        grade = self.env['eagleedu.exam.grading'].search([('score', '<=', gp)], limit=1,
                                                             order='score DESC')
        return grade.result
