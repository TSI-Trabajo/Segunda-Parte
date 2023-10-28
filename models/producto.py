# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
    _name = 'upobarber.producto'
    _description = 'Productos de UpoBarber'

    producto_id = fields.Char(string="ID Producto", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    precio = fields.Float(string="Precio")
    photo=fields.Binary('Photo')

    tipo_producto_id = fields.Many2one('upobarber.tipo_producto', string="Tipo de Producto", required=True)
    articulo_id = fields.Many2one('upobarber.articulo', string="Artículo Relacionado", required=True)