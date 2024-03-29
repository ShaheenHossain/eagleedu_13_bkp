# -*- coding: utf-8 -*-

{
    'name': "Eagle Education exam",
    'version': '13.0.0.1',
    'summary': """This is a Eagle eEducation exam management system""",
    'description': """
This module for This is a eagle erp eEducation exam management system 
    """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'category': 'Education',
    'depends': [ 'base', 'eagleedu_core'],
    'data':[
            'views/eagleedu_exam.xml',
            'views/eagleedu_exam_valuation.xml',
            'views/eagleedu_exam_grading.xml',
            'views/eagleedu_exam_results.xml',
            'security/ir.model.access.csv',
            # 'reports/print_reports.xml',
            # 'reports/report_eagleedu_registration.xml',
            # 'data/eagleedu.bddivision.csv',
    ],
    'installable' : True,
    'application' : False,
}

