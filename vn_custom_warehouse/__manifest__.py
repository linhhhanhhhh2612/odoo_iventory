{
    'name': 'VN Custom Warehouse',
    'version': '1.0',
    'depends': ['stock', 'hr'], 
    # TÔI ĐÃ XÓA SẠCH PHẦN DATA ĐỂ KHÔNG BỊ LỖI XML
    'data': [
        'security/ir.model.access.csv', 
        'views/stock_picking_views.xml',  # <-- BỎ dấu # đi
        'views/menu_views.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}