{
    'name': 'Purchase pricelists',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Use same pricelist model for sale and purchase''',
    'depends': [
        'purchase',
        'sale',
    ],
    'data':
        [
            'views/product_pricelist_sale.xml',
            'views/purchase_order.xml',
            'views/res_partner.xml',
            'views/menu.xml',
        ],
    'installable': True
}
