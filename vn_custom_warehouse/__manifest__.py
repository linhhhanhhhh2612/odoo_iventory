# -*- coding: utf-8 -*-
{
    'name': 'VN Custom Warehouse',
    'version': '1.0',
    'summary': 'Quản lý kho theo quy trình tùy chỉnh',
    'description': """
        Module quản lý kho với cấu trúc menu riêng:
        - Phân loại giao dịch (Tạm ứng, Hoàn ứng...)
        - Quy trình duyệt (Thủ kho, Kế toán)
    """,
    'author': 'YourName',
    'category': 'Inventory',
    'depends': ['stock', 'hr'], # Phụ thuộc module Kho và Nhân sự
    'data': [
        'security/ir.model.access.csv',
        'views/stock_picking_views.xml', # Load giao diện phiếu trước
        'views/menu_views.xml',          # Load menu sau
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}