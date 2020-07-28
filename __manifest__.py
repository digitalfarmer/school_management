{
    'name': 'School Management',
    'version': '12.0.1.0.0',
    'summary': 'Module for Manage School',
    'description': """ 
    Feature Module \n
        - Manage Teacher 
        - Manage Student 
        - Manage Staff
    """,
    'category': 'Extra Tools',
    'author': 'LobotIjo',
    'maintainer':'AdesDev',
    'website': 'digitalfarmer.github.io',
    'license': 'AGPL-3',
    'depends': [
        'base',

    ],
    'data': [
        'views/student.xml',
        'security/ir.model.access.csv'
    ],
    #'demo': [''],
    'installable': True,
    'application': True,
    'sequence': '1',
    'auto_install': False,

}