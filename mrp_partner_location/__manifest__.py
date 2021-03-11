{
    'name': 'Manufacturing Partner Location',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Add partner location to production orders''',
    'depends': [
        'mrp_partner',
        'base_location',
    ],
    'data': ['views/mrp_production.xml', ],
    'installable': True
}
