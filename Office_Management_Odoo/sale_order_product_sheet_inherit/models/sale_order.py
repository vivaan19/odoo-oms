# -*- coding: utf-8 -*-
from odoo import models, fields, api

class InheritSaleOrder(models.Model):
    # _inherit = "sale.order.line"
    _inherit = "sale.order"

    sample_field = fields.Char("sample_sale_order_field")

    # @api.onchange('price_unit')
    # def _onchange_price_unit(self):

    #     print("\n")
    #     print("on change price unit working ---------------->>>>>>> ")
    #     print("\n")

    #     # self.env['product.product'].search([('id', '=', self.product_id.id)], limit=1).update()
    #     self.env['product.product'].browse(self.product_id.id).write({'lst_price': self.price_unit})
    
    # @api.onchange('order_line.product_id')
    # def _onchange_partner_id(self):
    #     print("---------->>>>", self.partner_id)
        
    #     ser  = self.env['sale.order'].search([('partner_id', '=', self.partner_id.id)])
    #     print(ser)

    #     for sale_id in ser:
    #         print("id --->>>>>", sale_id)
            
    #         print("\n")

    #         print("sale product id ------->>>>>>>", sale_id.order_line.product_id)
    #         print("sale product id ------->>>>>>>", self.order_line.product_id)

    #         if sale_id.order_line.product_id ==  self.order_line.product_id:
    #             print("------------>>>> yes", max(sale_id))

        # if self.partner_id:


    
    # @api.model
    # def create(self, values):

    #     """
    #         Create a new record for a model InheritSaleOrder
    #         @param values: provides a data for new record
    
    #         @return: returns a id of new record
    #     """

        
    #     result = super(InheritSaleOrder, self).create(values)
    
    #     return result

class InheritSaleOrderLine(models.Model):
    _inherit = "sale.order.line"

    @api.onchange('product_id')
    def _onchange_product_id(self):
        print("---------->>>>", self.product_id)
        
        order  = self.env['sale.order'].search([('partner_id', '=', self.order_id.partner_id.id), ('order_line.product_id', '=', self.product_id.id)], limit=1)
        print(order)
        
        self.order_id.payment_term_id = order.payment_term_id
        self.price_unit = order.order_line.price_unit   

        # for sale_id in ser:
        #     print("id --->>>>>", sale_id)
            
            # print("\n")

            # print("sale product id ------->>>>>>>", self.product_id)
            # print("sale product id ------->>>>>>>", self.product_id)

            # if self.product_id ==  .product_id:
            #     print("------------>>>> yes", max(sale_id))

    
