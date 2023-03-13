# -*- coding: utf-8 -*-
# from odoo import http


# class SaleOrderProductSheetInherit(http.Controller):
#     @http.route('/sale_order_product_sheet_inherit/sale_order_product_sheet_inherit', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sale_order_product_sheet_inherit/sale_order_product_sheet_inherit/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('sale_order_product_sheet_inherit.listing', {
#             'root': '/sale_order_product_sheet_inherit/sale_order_product_sheet_inherit',
#             'objects': http.request.env['sale_order_product_sheet_inherit.sale_order_product_sheet_inherit'].search([]),
#         })

#     @http.route('/sale_order_product_sheet_inherit/sale_order_product_sheet_inherit/objects/<model("sale_order_product_sheet_inherit.sale_order_product_sheet_inherit"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sale_order_product_sheet_inherit.object', {
#             'object': obj
#         })
