# -*- coding: utf-8 -*-

{
    'name': "Eagle Education Core",
    'version': '1.1',
    'summary': """This is a e education manament system""",
    'description': """
This module for This is a e education manament system 
    """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'category': 'Education',
    'depends': [ 'base', ],
    'data':[
            'views/eagleedu_register.xml',
            'views/eagleedu_application.xml',
            'views/eagleedu_student.xml',
            'views/eagleedu_assigning_class.xml',
            'views/eagleedu_instructor.xml',
            # 'views/eagleedu_main_menu.xml',
            'views/eagleedu_class_division.xml',
            'views/eagleedu_academic_year.xml',
            'views/eagleedu_standard_class.xml',
            'views/eagleedu_class_section.xml',
            'views/eagleedu_class_category.xml',
            'views/eagleedu_group_division.xml',
            'views/eagleedu_class_history.xml',
            'views/eagleedu_subject.xml',
            'views/eagleedu_syllabus.xml',
            'security/ir.model.access.csv',
            'reports/print_reports.xml',
            'reports/report_eagleedu_registration.xml',
            # 'data/eagleedu.bddivision.csv',
    ],
    'installable' : True,
    'application' : False,
}

