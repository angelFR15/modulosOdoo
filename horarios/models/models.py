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
from typing_extensions import Required


class horario(models.Model):
    _name = 'horarios.horario'
    _description = 'Define los atributos de un horario'

    #atributos
    nombreHorario = fields.Char(string='Nombre horario', required = True)
    lunesEntrada = fields.Date (string='Hora entrada Lunes')
    lunesSalida = fields.Date(string='Hora salida Lunes')

    #relacion entre tablas
    empleado_id = fileds.One2many('proyectos.empleado', 'horario_id')