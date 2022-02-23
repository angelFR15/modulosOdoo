# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class horarios(models.Model):
#     _name = 'horarios.horarios'
#     _description = 'horarios.horarios'

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

class horario(models.Model):
    _name = 'horarios.horario'
    _description = 'horarios.horario'

    #atrib
    nombreHorario = fields.Char(string='Nombre horario', required=True)
    lunesEntrada = fields.Date(string='Hora entrada Lunes')
    lunesSalida = fields.Date(string='Hora entrada Lunes')

    #relacion entre tablas
    empleado_id = fields.One2mane('proyectos.empleado', 'horario_id', string="Horario")