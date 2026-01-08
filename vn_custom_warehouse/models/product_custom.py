from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    # Tạo thêm cột Ngưỡng báo động (Mặc định là 0)
    x_min_quantity = fields.Float(string='Ngưỡng báo động (Min)', default=0, 
                                 help='Nếu tồn kho nhỏ hơn số này, hệ thống sẽ cảnh báo đỏ')
