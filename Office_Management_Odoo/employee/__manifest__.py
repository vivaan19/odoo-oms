{
    'name': "Office Management System-Employee Section",
    'version': '1.0.0',
    'sequence': -100,
    'depends': ['base', 'mail'],
    # to add chatter field add mail to depends
    'author': "Vivaan",
    'category': 'Category',
    'data' : [
        'security/ir.model.access.csv',
        'views/office_emp.xml',
        'menu/office_employee_menu.xml',
        'views/emp_attendance.xml', 
        # 'menu/office_employee_menu.xml',
        'views/emp_hobby.xml',
    ],

    'demo' : [],
    'license' : 'AGPL-3',
    'auto_install' : False, 
    'application':True,
    'summary' : "Office management system for employees", 
    'description': """ Office Management system for employees""", 

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