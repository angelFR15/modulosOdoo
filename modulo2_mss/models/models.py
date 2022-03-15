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
    _name = 'modulo2_mss.entrega'
    _description = 'Define los atributos de la entrega.'

    refEntrega = fields.Char(string='Referencia', required=True)
    fechaEntrega = fields.Date(string="Fecha Entrega", required=True)
    unidades = fields.Integer(string="Unidades", required=True)
    entregaRealizada = fields.Boolean(string='Realizada', default=False)

    producto_id = fields.Many2many('modulo1_mss.producto',string='Producto')
    reparto_id = fields.Many2one('modulo2_mss.reparto', string='Compania de reparto')

class reparto(models.Model):
    _name = 'modulo2_mss.reparto'
    _description = 'Define los atributos de la compañia de reparto.'

    nifR = fields.Char(string='NIF', required=True)
    nombreR = fields.Char(string='Nombre', required=True)
    paisR = fields.Char(string='Pais', required=True)

    entrega_id = fields.One2many('modulo2_mss.entrega','reparto_id', string='Entrega')