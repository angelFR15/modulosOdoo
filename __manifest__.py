# -*- coding: utf-8 -*-
{
    'name': "Modulos Odoo",

    'summary': """
        Esta aplicacion es una prueba de funcionamiento.""",

    'description': """
        Media Shop Spain es una tienda de tecnologia: Ordenadores, moviles, consolas.... Tenemos de todo!
        Por lo que necesitamos tener nuestros m�dulos actualizados.
    """,

    'author': "Angel MMS",
    'website': "http://infsalinas.sytes.net:10070/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tecnolog�a',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'application' : True,
}
