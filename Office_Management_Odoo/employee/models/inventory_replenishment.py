from odoo import models, fields, api 

class InventoryReplenishment(models.Model):
    _inherit = "stock.warehouse.orderpoint"
    