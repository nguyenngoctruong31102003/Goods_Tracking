from odoo import models, fields
import logging  # Nhập thư viện logging để ghi lại thông tin và lỗi
_logger = logging.getLogger(__name__)  # Tạo logger để ghi lại thông tin

class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'
    # test = fields.Boolean(string="Test")
    res_partner_id = fields.Many2one("res.partner",string="Chủ sở hữu")