{
    'name': 'VN Custom Warehouse',
    'version': '1.0',
    'category': 'Inventory',
    'summary': 'Quan ly kho tuy chinh cho Viet Nam',
    'depends': ['stock'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml',
        'views/product_views.xml',    # <-- FILE MỚI
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
}
