# -*- coding: utf-8 -*-
{
    'name': "upobarber",

    'summary': """Gestion del modulo upobarber""",

    'description': """Gestion de peluqueria.""",

    'author': "TSI - UPO",
    'website': "https://www.upo.es",

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
        'views/tipoproducto_views.xml',
        'views/menu.xml',
        
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo/demo.xml',
        'demo/upobarber.articulo.csv',
        'demo/upobarber.producto.csv',
        'demo/upobarber.tipoproducto.csv',
    ],
    'application': True,
}
