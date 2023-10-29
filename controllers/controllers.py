# -*- coding: utf-8 -*-
# from odoo import http


# class UpoBarber(http.Controller):
#     @http.route('/upo_barber/upo_barber', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upo_barber/upo_barber/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('upo_barber.listing', {
#             'root': '/upo_barber/upo_barber',
#             'objects': http.request.env['upo_barber.upo_barber'].search([]),
#         })

#     @http.route('/upo_barber/upo_barber/objects/<model("upo_barber.upo_barber"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upo_barber.object', {
#             'object': obj
#         })
