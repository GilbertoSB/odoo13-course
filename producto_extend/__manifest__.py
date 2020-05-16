# -*- coding: utf-8 -*-
{
    'name': "Product Material",

    'summary': """
        Producto extend es un ejemplo de la herencia en odoo
        Se agrega un campo slection como ejemplo practico""",

    'description': """
        Practicar lo aprendido en el curso de Odoo 13 sobre la herencia
    """,

    'author': "SaitCloud",
    'website': "http://www.saitcloud.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Product',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['product'],

    # always loaded
    'data': [
        'views/product_view.xml',
    ],
    'installable': True,
    'application': True,
}
