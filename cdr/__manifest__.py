# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'CDR',
    'summary': ' Modulo para carga de CDR',

    'description': """
    - Permite la cargad de un CDR para la generaciónde facturas.
    """,
    'author': "Xmarts, Nayeli Valencia Díaz",
    'website': "http://www.xmarts.com",
    'depends': ['base','sale_subscription'],
    'data': [
        'views/cdr.xml'
    ]
}
