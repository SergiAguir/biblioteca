# -*- coding: utf-8 -*-
{
    'name': "biblioteca",

    'summary': """
        Aplicacion de una biblioteca""",

    'description': """
        Aplicacion de una biblioteca
    """,

    'author': "Sergi Agüir",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/biblioteca_security.xml',
        'security/ir.model.access.csv',
        'views/prestamo_view.xml',
        'views/premio_view.xml',
        'views/genero_view.xml',
        'views/libro_view.xml',
        'views/autor_view.xml',
        'views/bibliotecario_view.xml',
        'views/socio_view.xml',
        'views/persona_view.xml',
        'views/menu_view.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application':True,
    'installable':True,
}
