from odoo import models, fields, api 

class InventoryReplenishment(models.Model):
    _inherit = "stock.warehouse.orderpoint"

    quantity_diff = fields.Float(string="Difference",compute="_compute_quantity_diff")

    def _compute_quantity_diff(self):
        for rec in self:
            rec.quantity_diff = rec.product_max_qty - rec.product_min_qty
            
    # @api.onchange('product_min_qty')
    # def _onchange_product_id(self):
    #     self.quantity_diff = self.product_max_qty - self.product_min_qty
    
    # @api.onchange('product_max_qty')
    # def _onchange_product_id(self):
    #     self.quantity_diff = self.product_max_qty - self.product_min_qty
    