# -*- coding: utf-8 -*-
{
    'name': "upobarber",

    'summary': """Gestion del modulo upobarber""",

    'description': """Gestion de articulos, productos, tipos de producto, etc.""",

    'author': "TSI-UPO",
    'website': "https://www.upo.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/articulo_views.xml',
        'views/producto_views.xml',
        'views/tipo_producto_views.xml',
        'views/menu.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/upobarber.resena.csv',
        'demo/upobarber.tipo_servicio.csv',
        'demo/upobarber.servicio.csv',    
    ],
}