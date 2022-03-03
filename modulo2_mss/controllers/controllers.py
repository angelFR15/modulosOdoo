# -*- coding: utf-8 -*-
# from odoo import http


# class Modulo2Mss(http.Controller):
#     @http.route('/modulo2_mss/modulo2_mss/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/modulo2_mss/modulo2_mss/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('modulo2_mss.listing', {
#             'root': '/modulo2_mss/modulo2_mss',
#             'objects': http.request.env['modulo2_mss.modulo2_mss'].search([]),
#         })

#     @http.route('/modulo2_mss/modulo2_mss/objects/<model("modulo2_mss.modulo2_mss"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('modulo2_mss.object', {
#             'object': obj
#         })
