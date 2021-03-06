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

class producto(models.Model):
    _name = 'modulo1_mss.producto'
    _description = 'Define los atributos del producto.'

    refProducto = fields.Char(string='Referencia', required=True)
    marca = fields.Char(string='Marca', required='True')
    tipoProducto = fields.Selection(string='Tipo de producto', required=True, selection=[('Electrodomestico', 'Electrodomestico'),('Telefono', 'Telefono'),('Ordenador portátil', 'Ordenador portátil'),('Ordenador torre', 'Ordenador torre'),('Consola', 'Consola')], help='Tipo del producto.')
    precioCompra = fields.Float('Precio compra', (4,2), required=True)
    precioVenta = fields.Float('Precio venta', (4,2), compute='_getPrecioV')

    proveedor_id = fields.Many2one('modulo1_mss.proveedor', string='Proveedor')
    almacen_id = fields.Many2one('modulo1_mss.almacen', string='Almacen')
    entrega_id = fields.Many2many('modulo2_mss.entrega', string='Entrega')

    @api.depends('precioCompra')
    def _getPrecioV(self):
        for producto in self:
            producto.precioVenta = producto.precioCompra + (producto.precioCompra * 0.21)

    @api.constrains('precioCompra')
    def _checkPrecioC(self):
        for producto in self:
            if (producto.precioCompra <= 0.0):
                raise exceptions.ValidationError("El precio no puede ser 0.")
    
class proveedor(models.Model):
    _name = 'modulo1_mss.proveedor'
    _description = 'Define los atributos del proveedor.'

    nifP = fields.Char(string='NIF', required=True)
    nombreProveedor = fields.Char(string='Nombre', required=True)
    paisProveedor = fields.Char(string='Pais', required=True)
    direccionProveedor = fields.Char(string='Direccion', required=True)

    producto_id = fields.One2many('modulo1_mss.producto','proveedor_id', string='Productos')

    def name_get(self):
        listaProveedores = []
        for proveedor in self:
            listaProveedores.append((proveedor.id,proveedor.nombreProveedor))
        return listaProveedores
    @api.constrains('nifP')
    def _checkNIF(self):
        for proveedor in self:
            if (len(proveedor.nifP) > 5 or len(proveedor.nifP) < 5):
                raise exceptions.ValidationError("El NIF se compone de 5 digitos")

class almacen(models.Model):
    _name = 'modulo1_mss.almacen'
    _description = 'Define los atributos del proveedor.'

    refAlmacen = fields.Char(string='Referencia', required=True)
    categoria = fields.Selection(string='Categoria', selection=[('Electrodomesticos', 'Electrodomesticos'),('Telefonos', 'Telefonos'),('Ordenadores', 'Ordenadores'),('Consolas', 'Consolas')], help='Indica la categoria del almacen.', required='True')
    pasillo = fields.Integer(string="Nº pasillo", required=True)

    producto_id = fields.One2many('modulo1_mss.producto','almacen_id', string='Productos')

    def name_get(self):
        listaAlmacenes = []
        for almacen in self:
            listaAlmacenes.append((almacen.id, almacen.refAlmacen + ", " + almacen.categoria))
        return listaAlmacenes

    @api.constrains('pasillo')
    def _checkPasillo(self):
        for almacen in self:
            if (almacen.pasillo > 5 or almacen.pasillo < 1):
                raise exceptions.ValidationError("Le recordamos que cada almacén tiene únicamente 5 pasillos (enumerados del 1 al 5).")