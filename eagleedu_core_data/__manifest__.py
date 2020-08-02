# -*- coding: utf-8 -*-

{
    'name': "Eagle Education Core Data",
    'version': '1.1',
    'summary': """This is a e education management data""",
    'description': """
This module for This is a e education management system 
    """,
    'author': "Eagle ERP",
    'website': "http://www.eagle-erp.com",
    'support': 'info@eagle-erp.com',
    'category': 'Education',
    'depends': [ 'base', 'eagleedu_core', ],
    'data':[
            # 'data/eagleedu.class.category.csv',
            'data/eagleedu.class_section.csv',
            'data/eagleedu.subject.csv',
            'data/eagleedu.group_division.csv',
            'data/eagleedu.roomnumber.csv',
            'data/eagleedu.roomname.csv',
            'data/eagleedu.standard_class.csv',
            # 'data/eagleedu.guardian.relation.csv',
            # 'data/eagleedu.bddistrict.csv',

            #'views/eagleedu_core_data.xml',
 
            # 'data/eagleedu.bddivision.csv',
    ],
    'installable' : True,
    'application' : False,
}

