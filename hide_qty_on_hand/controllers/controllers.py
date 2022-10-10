# -*- coding: utf-8 -*-
# from odoo import http


# class HideQtyOnHand(http.Controller):
#     @http.route('/hide_qty_on_hand/hide_qty_on_hand', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hide_qty_on_hand/hide_qty_on_hand/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('hide_qty_on_hand.listing', {
#             'root': '/hide_qty_on_hand/hide_qty_on_hand',
#             'objects': http.request.env['hide_qty_on_hand.hide_qty_on_hand'].search([]),
#         })

#     @http.route('/hide_qty_on_hand/hide_qty_on_hand/objects/<model("hide_qty_on_hand.hide_qty_on_hand"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hide_qty_on_hand.object', {
#             'object': obj
#         })
