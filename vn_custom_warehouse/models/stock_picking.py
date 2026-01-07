from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    # Khai bao cac cot du lieu (Field)
    x_transaction_type = fields.Selection([
        ('tam_ung', 'Tam ung vat tu'),
        ('hoan_ung', 'Hoan ung vat tu'),
        ('cap_linh_kien', 'Cap linh kien'),
        ('nhap_hong', 'Nhap linh kien hong'),
        ('cap_san_xuat', 'Cap vat tu san xuat'),
        ('tra_lai', 'Nhap kho hang tra lai'),
        ('xuat_kinh_doanh', 'Xuat kho kinh doanh'),
        ('chuyen_noi_bo', 'Chuyen kho noi bo'),
        ('xuat_doi', 'Xuat doi cau hinh'),
        ('khac', 'Khac')
    ], string='Muc dich nghiep vu', default='khac')

    x_approval_state = fields.Selection([
        ('draft', 'Moi tao'),
        ('waiting_warehouse', 'Cho Thu kho duyet'),
        ('waiting_accountant', 'Cho Ke toan duyet'),
        ('approved', 'Hoan thanh'),
        ('rejected', 'Tu choi')
    ], string='Tien trinh duyet', default='draft')

    def action_send_warehouse(self):
        self.write({'x_approval_state': 'waiting_warehouse'})

    def action_approve_warehouse(self):
        self.write({'x_approval_state': 'waiting_accountant'})

    def action_approve_accountant(self):
        self.write({'x_approval_state': 'approved'})

    def action_open_oca_scanner(self):
        return
    def action_open_oca_scanner(self):
        self.ensure_one()
        # Thay vì mở Client Action (cần module xịn), ta mở View Chi tiết (có sẵn)
        return {
            'name': 'Chi tiết hoạt động',
            'type': 'ir.actions.act_window',
            'view_mode': 'list,form',
            'res_model': 'stock.move.line', # Mở bảng chi tiết dòng
            'domain': [('picking_id', '=', self.id)], # Lọc theo phiếu hiện tại
            'context': {'default_picking_id': self.id},
            'target': 'current',
        }