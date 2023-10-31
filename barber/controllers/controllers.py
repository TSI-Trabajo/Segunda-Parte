# -*- coding: utf-8 -*-
# from odoo import http


# class Barber(http.Controller):
#     @http.route('/barber/barber', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/barber/barber/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('barber.listing', {
#             'root': '/barber/barber',
#             'objects': http.request.env['barber.barber'].search([]),
#         })

#     @http.route('/barber/barber/objects/<model("barber.barber"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('barber.object', {
#             'object': obj
#         })
