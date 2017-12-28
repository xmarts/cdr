# -*- coding: utf-8 -*-
{
    'name': "CDR",

    'summary': """
       Modulo para carga de CDR""",

    'description': """
    - Permite la cargad de un CDR para la generaciónde facturas.
    """,

    'author': "Xmarts, Nayeli Valencia Díaz",
    'website': "http://www.xmarts.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale_subscription'],
    # always loaded
    'data': [
        'model/cdr.xml'
    ]
}
