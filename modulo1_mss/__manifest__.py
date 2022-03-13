# -*- coding: utf-8 -*-
{
    'name': "Inventario Interno MSS",

    'summary': """
        Aplicacion para y de la empresa Media Shop Spain.""",

    'description': """
        Este módulo se utilizará para registrar productos, almacenes donde se destinarán los productos y los pasillos en los que se encuentren.""",

    'author': "Media Shop Spain, Angel Fernandez",
    'website': "http://infsalinas.sytes.net:10070",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tecnologia',
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
