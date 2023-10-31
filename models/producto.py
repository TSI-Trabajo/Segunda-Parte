# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Producto(models.Model):
    _name = 'upobarber.producto'
    _description = 'Productos de UpoBarber'

    producto_id = fields.Integer(string="ID Producto", required=True, index=True)

    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    foto = fields.Binary('Foto')

    articulo_ids = fields.One2many('upobarber.articulo', 'producto_id', string="Artículos Relacionados")
    #tipoproducto_id = fields.Many2one('upobarber.tipoproducto', string="Tipo de Producto")