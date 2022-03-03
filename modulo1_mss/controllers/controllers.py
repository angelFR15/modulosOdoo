# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo1Mss(http.Controller):
#     @http.route('/modulo1_mss/modulo1_mss/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo1_mss/modulo1_mss/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo1_mss.listing', {
#             'root': '/modulo1_mss/modulo1_mss',
#             'objects': http.request.env['modulo1_mss.modulo1_mss'].search([]),
#         })

#     @http.route('/modulo1_mss/modulo1_mss/objects/<model("modulo1_mss.modulo1_mss"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo1_mss.object', {
#             'object': obj
#         })
