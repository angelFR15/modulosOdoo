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
from datetime import date, datetime
from dateutil.relativedelta import *

class bajas(models.Model):
    _name = 'horarios.bajas'
    _description = 'Define los atributos de la baja'

    motivoBaja = fields.Selection(string='Motivo de la baja:', Selection=[('a','Enfermedad'),('b','Maternidad'),('c','Paternidad'),('d','Accidente')])
    gravedadBaja = fields.Selection(string='Gravedad de la baja:',Selection=[('a','Muy grave'),('b','Grave'),('c','Normal'),('d','Leve')])
    descripcionBaja = fields.Text(string='Descripcion de la baja:', required=True, help='Escribe una descripcion detallada')
    fechaBaja = fields.Date(string='Fecha de la baja', required=True, default=fields.Date.today())

    empleado_id = fields.Many2one('proyectos.empleado','empleado.baja_id')

class horarios(models.Model):
    _name = 'horarios.horario'
    _description = 'Define los atributos de un horario'

    #atributos
    nombreHorario = fields.Char(string='Nombre horario', required = True)

    lunesEntrada = fields.Selection(string='Hora entrada lunes', selection='_get_valid_hours', default='8')
    lunesSalida = fields.Selection(string='Hora salida lunes', selection='_get_valid_hours', default='8')
    martesEntrada = fields.Selection(string='Hora entrada martes', selection='_get_valid_hours', default='8')
    martesSalida = fields.Selection(string='Hora salida martes', selection='_get_valid_hours', default='8')
    miercolesEntrada = fields.Selection(string='Hora entrada miercoles', selection='_get_valid_hours', default='8')
    miercolesSalida = fields.Selection(string='Hora salida miercoles', selection='_get_valid_hours', default='8')
    juevesEntrada = fields.Selection(string='Hora entrada jueves', selection='_get_valid_hours', default='8')
    juevesSalida = fields.Selection(string='Hora salida jueves', selection='_get_valid_hours', default='8')
    viernesEntrada = fields.Selection(string='Hora entrada viernes', selection='_get_valid_hours', default='8')
    viernesSalida = fields.Selection(string='Hora salida viernes', selection='_get_valid_hours', default='8')

    #relacion con tabla empleados
    empleado_id = fields.One2many('proyectos.empleado','horario_id')

    def name_get(self):
        resultados=[]
        for horario in self:
            resultados.append((horario.id, horario.nombreHorario))
        return resultados

    @api.model
    def _get_valid_hours(self):
        selection = [
            ('8', '8:00'),   ('8.5', '8:30'),
            ('9', '9:00'),   ('9.5', '9:30'),
            ('10', '10:00'), ('10.5', '10:30'),
            ('11', '11:00'), ('11.5', '11:30'),
            ('12', '12:00'), ('12.5', '12:30'),
            ('13', '13:00'), ('13.5', '13:30'),
            ('14', '14:00'), ('14.5', '14:30'),
            ('15', '15:00'), ('15.5', '15:30'),
            ('16', '16:00'), ('16.5', '16:30'),
            ('17', '17:00'), ('17.5', '17:30'),
            ('18', '18:00')
        ]
        return selection

    @api.constrains('lunesEntrada','martesEntrada','miercolesEntrada','juevesEntrada','viernesEntrada')
    def change_data_field(self):
        hel = float(self.lunesEntrada)
        hsl = float(self.lunesSalida)
        if(hel >= hsl):
            raise exceptions.ValidationError("Las horas del Lunes estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")
        
        hem = float(self.martesEntrada)
        hsm = float(self.martesSalida)
        if(hem >= hsm):
            raise exceptions.ValidationError("Las horas del Martes estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")
        
        hex = float(self.miercolesEntrada)
        hsx = float(self.miercolesSalida)
        if(hex >= hsx):
            raise exceptions.ValidationError("Las horas del Miercoles estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")

        hex = float(self.miercolesEntrada)
        hsx = float(self.miercolesSalida)
        if(hex >= hsx):
            raise exceptions.ValidationError("Las horas del Miercoles estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")

        hej = float(self.juevesEntrada)
        hsj = float(self.juevesSalida)
        if(hej >= hsj):
            raise exceptions.ValidationError("Las horas del Jueves estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")

        hev = float(self.viernesEntrada)
        hsv = float(self.viernesSalida)
        if(hev >= hsv):
            raise exceptions.ValidationError("Las horas del Viernes estan mal, revisalas (la hora de salida no puede ser anterior o igual a la de entrada).")