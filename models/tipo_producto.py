# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoProducto(models.Model):
    _name = 'upobarber.tipo_producto'
    _description = 'Tipo de Producto'

    tipo_producto_id = fields.Char(string="ID Tipo Producto", required=True)
    nombre = fields.Char(string="Nombre", required=True)