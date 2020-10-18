{
    'name': 'Product Reference',
    'version': '12.0.1.0.0',
    'author': 'DEC, Yann Papouin',
    'website': 'http://www.dec-industrie.com',
    'summary': '''Product reference management''',
    'depends': [
        'base',
        'uom',
        'product',
        'mrp',
        'product_reference_management',
        'product_state_review',
        'product_location',
        'product_prices',
        'product_legacy_routes',
        'product_tagging',
        'product_pack_order_type',
        'product_public_code',
        'mrp_production_request',
        'mrp_bom_dates',
        'mrp_bom_supplier',
        'mrp_bom_prices',
        'sale_purchase',
        'sale_timesheet',
    ],
    'data':
        [
            'security/model_security.xml',
            'security/ir.model.access.csv',
            'views/product_template.xml',
            'views/product_product.xml',
            'views/ref_attribute.xml',
            'views/ref_property.xml',
            'views/ref_reference.xml',
            'views/ref_reference_line.xml',
            'views/ref_category.xml',
            'views/ref_category_line.xml',
            'views/ref_version.xml',
            'views/menu.xml',
        ],
    'installable': True
}
