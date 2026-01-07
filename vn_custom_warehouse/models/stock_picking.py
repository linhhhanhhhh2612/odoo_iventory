from odoo import models, fields, api

class StockPicking(models.Model):
    _inherit = 'stock.picking' # Dòng này xác nhận chúng ta đang dùng lại module gốc

    # 1. Phân loại mục đích (để lọc Menu A)
    x_transaction_type = fields.Selection([
        ('tam_ung', 'Tạm ứng vật tư'),
        ('hoan_ung', 'Hoàn ứng vật tư'),
        ('cap_linh_kien', 'Cấp linh kiện'),
        ('nhap_hong', 'Nhập linh kiện hỏng'),
        ('cap_san_xuat', 'Cấp vật tư sản xuất'),
        ('tra_lai', 'Nhập kho hàng trả lại'),
        ('xuat_kinh_doanh', 'Xuất kho kinh doanh'),
        ('chuyen_noi_bo', 'Chuyển kho nội bộ'),
        ('xuat_doi', 'Xuất đổi cấu hình'),
        ('khac', 'Khác')
    ], string='Mục đích nghiệp vụ', default='khac')

    # 2. Trạng thái duyệt (để lọc Menu B)
    x_approval_state = fields.Selection([
        ('draft', 'Mới tạo'),
        ('waiting_warehouse', 'Chờ Thủ kho duyệt'),
        ('waiting_accountant', 'Chờ Kế toán duyệt'),
        ('approved', 'Hoàn thành'),
        ('rejected', 'Từ chối')
    ], string='Tiến trình duyệt', default='draft', tracking=True)

    # Các hàm xử lý nút bấm
    def action_send_warehouse(self):
        self.write({'x_approval_state': 'waiting_warehouse'})

    def action_approve_warehouse(self):
        self.write({'x_approval_state': 'waiting_accountant'})

    def action_approve_accountant(self):
        self.write({'x_approval_state': 'approved'})