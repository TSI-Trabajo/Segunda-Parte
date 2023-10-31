# -*- coding: utf-8 -*-

from odoo import models, fields, api

class TipoProducto(models.Model):
    _name = 'upobarber.tipoproducto'
    _description = 'Tipo de Producto'

    tipoproducto_id = fields.Integer(string="ID Tipo Producto", required=True, index=True)
    nombre = fields.Char(string="Nombre", required=True)

    #articulo_ids = fields.One2many('upobarber.articulo', 'tipoproducto_id', string="Artículos Relacionados")