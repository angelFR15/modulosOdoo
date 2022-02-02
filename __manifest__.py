# -*- coding: utf-8 -*-
{
    'name': "Modulos Odoo",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Media Shop Spain es una tienda de tecnología: Ordenadores, móviles, consolas.... ¡Tenemos de todo!
        Por lo que necesitamos tener nuestros módulos actualizados.
    """,

    'author': "Angel MMS",
    'website': "http://infsalinas.sytes.net:10070/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tecnología',
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
}
