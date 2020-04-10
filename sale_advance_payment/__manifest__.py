# -*- coding: utf-8 -*-
{

    'name': "Sale Advance Payment",
    'version': '1.1',
    'category': 'Accounting',
    'author': 'RDFlex',
    'website': 'https://rdflex.com',
    'summary': 'Sale Advance Payment',
    'description': """
Sale Advance Payment
====================
    """,
    'depends': ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/sale_order_view.xml',
        'wizard/sale_advance_payment_wizard.xml',
             ],
    'installable': True,
    'auto_install': False,
}
