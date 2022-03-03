# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulo1_mss(models.Model):
#     _name = 'modulo1_mss.modulo1_mss'
#     _description = 'modulo1_mss.modulo1_mss'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
