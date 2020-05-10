# -*- coding: utf-8 -*-
{
    'name': "Library Managment",

    'summary': """
        Library es un modulo creado durante el curso de Odoo 13
        dicho curso impartido por Juan Carlos Montoya""",

    'description': """
        Practicar lo aprendido en el curso de Odoo 13
    """,

    'author': "SaitCloud",
    'website': "http://www.saitcloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tools',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'views/library_book_view.xml',
        'views/library_category_view.xml',
        'views/library_author_view.xml',
        'views/library_menu.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': True,
}
