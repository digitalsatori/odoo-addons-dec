{
    'name': 'Manufacturing Buy Consumables',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': "Choose if consummables must be bought or just reserved",
    'depends': [
        'product',
        'mrp',
    ],
    'data': ['views/mrp_bom.xml', ],
    'installable': True
}
