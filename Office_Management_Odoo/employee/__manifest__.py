{
    'name': "Office Management System-Employee Section",
    'version': '1.0.0',
    'sequence': -100,
    'depends': ['base', 'mail', 'stock', 'website'],
    # to add chatter field add mail to depends
    'author': "Vivaan",
    'category': 'Category',
    

  

    'data' : [
        # always load security, views, menu
        'security/ir.model.access.csv',
        'data/employee_apply.xml',
        'wizards/cancel_emp_transient_model.xml',
        'views/office_emp.xml',
        'views/emp_attendance.xml', 
        # 'menu/office_employee_menu.xml',
        'views/emp_hobby.xml',
        'views/emp_join.xml',
        'views/candidate_review.xml',
        'views/inventory_rep_color.xml',
        'views/inherit_shop_address.xml',
        'report/employee_detail_report.xml',
        'report/employee_details.xml',
        'menu/office_employee_menu.xml',

    ],


    'demo' : [],
    'license' : 'AGPL-3',
    'auto_install' : False, 
    'application':True,
    'summary' : "Office management system for employees", 
    'description': """ Office Management system for employees """, 

    # Description text
    # data files always loaded at installation
    # 'data': [
    #     'data/.xml',
    # ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}