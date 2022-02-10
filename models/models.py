# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class proyectos(models.Model):
#     _name = 'proyectos.proyectos'
#     _description = 'proyectos.proyectos'

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

class departamento(models.Model):
	_name = 'proyectos.departamento'
	_description = 'Define los atributos de un departamento'

	#atributos
	nombreDpto = fields.Char(string='Nombre departamento', required=True)

	#Relacion entre tablas
	empleado_id = fields.One2many('proyectos.empleado','departamento_id', string='Departamento')


class empleado(models.Model):
	_name = 'proyectos.empleado'
	_description = 'Define los atributos de un empleado'

	#atributos
	dniEmpleado = fields.Char(string='DNI', required=True)
	nombreEmpleado = fields.Char(string='Nombre', required=True)
	fechaNacimiento = fields.Date(string='Fecha nacimiento', required=True, default=fields.date.today())
	direccionEmpleado = fields.Char(string='Direccion', required=True)
	telefonoEmpleado = fields.Char(string='Telefono')
	edad = fields.Integer(string='Edad', compute='_getEdad')

	@api.depends('fechaNacimiento')
	def _getEdad(self):
		hoy = date.today()
		for empleado in self:
			empleado.edad = relativedelta(hoy, empleado.fechaNacimiento).years

	@api.constrains('dniEmpleado')
	def _checkDNI(self):
		for empleado in self:
			if (len(empleado.dniEmpleado) > 9):
				raise exceptions.ValidationError("El DNI no puede contener mas de 9 caracteres.")
			if (len(empleado.dniEmpleado) < 9)
				raise exceptions.ValidationError("El DNI no puede contener menos de 9 caracteres.")

	#Relacion entre tablas
	departamento_id = fields.Many2one('proyectos.departamento', string='Departamento')
	proyecto_id = fields.Many2many('proyectos.proyecto', string='Proyectos')

class proyecto(models.Model):
	_name = 'proyectos.proyecto'
	_description = 'Atributos de un proyecto'

	#atributos
	nombreProyecto = fields.Char(string='Nombre proyecto', required=True)
	tipoProyecto = fields.Selection(string='Tipo de proyecto', selection=[('f', 'Front-End'),('b', 'Back-End')], help='Tipo de proyecto al que esta destinado')
	descripcionProyecto = fields.Char(string='Descripcion del proyecto')
	fechaInicio = fields.Date(string="Fecha Inicio", Required=True)
	fechaFinal = fields.Date(string="Fecha Final", Required=True)

	@api.depends('fechaInicio')
	def _checkFechaInicio(self):
		hoy = date.today()
		for proyecto in self:
			proyecto.fechaInicio
			dias = relativedelta(hoy, proyecto.fechaInicio).days
			if (dias < 0):
				raise.exceptions.ValidationError("La fecha no puede ser anterior a hoy.")

	#Relacion entre tablas
	empleado_id = fields.Many2many('proyectos.empleado', string='Empleados')