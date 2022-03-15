# -*- coding: utf-8 -*-
{
    'name': "Entregas y Reparto",

    'summary': """
        Aplicacion para y de la empresa Media Shop Spain.
        """,

    'description': """
        Este módulo se basa en las entregas que recibimos de los productos y de las empresas de reparto asociadas.
    """,

    'author': "Media Shop Spain, Angel Fernandez",
    'website': "http://infsalinas.sytes.net:10070",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Tecnologia',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','modulo1_mss'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'report/modulo2_mss_idEntrega_report.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
