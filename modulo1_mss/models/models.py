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
from odoo import models, fields, api, exceptions
from datetime import date
from dateutil.relativedelta import *

class producto(models.Model):
    _name = 'modulo1_mss.producto'
    _description = 'Define los atributos del producto.'

    refProducto = fields.Char(string='Referencia', required=True)
    marca = fields.Char(string='Marca', required='True')
    tipoProducto = fields.Selection(string='Tipo de producto', selection=[('a', 'Electrodomestico'),('b', 'Telefono'),('c', 'Ordenador portátil'),('d', 'Consola')], help='Tipo del producto.')
    precioCompra = fields.Decimal(string='Precio compra', required=True)
    precioVenta = fields.Double(string='Precio venta', required=True)

    proveedor_id = fields.Many2one('modulo1_mss.proveedor', string='Proveedor')
    almacen_id = fields.Many2one('modulo1_mss.almacen', string='Almacen')


    
class proveedor(models.Model):
    _name = 'modulo1_mss.proveedor'
    _description = 'Define los atributos del proveedor.'

    nifP = fields.Char(string='NIF', required=True)
    nombreProveedor = fields.Char(string='Nombre', required=True)
    paisProveedor = fields.Char(string='Pais', required=True)
    direccionProveedor = fields.Char(string='Direccion', required=True)

    def name_get(self):
        listaProveedores = []
        for proveedor in self:
            listaProveedores.append((proveedor.id,proveedor.nombreProveedor))
        return listaProveedores

class almacen(models.Model):
    _name = 'modulo1_mss.almacen'
    _description = 'Define los atributos del proveedor.'

    refAlmacen = fields.Char(string='Referencia', required=True)
    categoria = fields.Selection(string='Categoria', selection=[('a', 'Electrodomestico'),('b', 'Telefono'),('c', 'Ordenador portátil'),('d', 'Consola')], help='Indica la categoria del almacen.')
    pasillo = fields.Integer(string="Nº pasillo", required=True)