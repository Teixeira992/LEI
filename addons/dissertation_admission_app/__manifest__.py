{'name': 'Aplicação para Admissão a Dissertação',
 'description': 'Gestão do processo de admissão à dissertação',
 'depends': ['base'],
 'data': [
     'security/dissertation_admission_security_groups.xml',
     'security/dissertation_admission_security_rules.xml',
     'security/ir.model.access.csv',
     'views/student_view.xml',
     'views/adviser_view.xml',
     'views/direction_view.xml',
     'views/dissertation_view.xml',
     'views/dissertation_admission_menu.xml',
     'demo/course.xml',
     'demo/department.xml',
     'demo/investigation_center.xml'
 ],
 'application': True,
 'installable': True,
 }
