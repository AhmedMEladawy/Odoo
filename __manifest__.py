{
    'name': "Hospital Management System App-Health",
    'description': """""",
    'author': "Ahmed Eladawy",
    'category': 'Health',
    'version': '17.0.0.1.0',
    'depends':['base'
               ],
    'application': True,
    'data': [
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient.xml',
        'views/doctor.xml',
        'views/department.xml'
        'wizard/add_log_wizard.xml'
    ]
}