# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class modulo2_mss(models.Model):
#     _name = 'modulo2_mss.modulo2_mss'
#     _description = 'modulo2_mss.modulo2_mss'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class entrega(models.Model):
    _name = 'modulo1_mss.entrega'
    _description = 'Define los atributos de la entrega.'

    refEntrega = fields.Char(string='Referencia', required=True)
    fechaEstimada = fields.Date(string="Fecha Estimada", required=True)
    unidades = fields.Integer(string="Unidades", required=True)
    entregaRealizada = fields.Boolean(string='Realizada', default=False)

class companiaReparto(models.Model):
    _name = 'modulo1_mss.companiaReparto'
    _description = 'Define los atributos de la compañia de reparto.'

    nifCR = fields.Char(string='NIF', required=True)
    nombreCR = fields.Char(string='Nombre', required=True)
    paisCR = fields.Char(string='Pais', required=True)