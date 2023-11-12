# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    name = fields.Integer(string="ID Compra")
    importe = fields.Float(string="Importe")
    fechaCompra = fields.Datetime(string="Fecha Compra")

    articulo_ids = fields.One2many('upobarber.articulo', 'compra_id', "Articulo")

    #pago_id = fields.related('upobarber.Pago', string="Pago")
    #cliente_id = fields.One2many('upobarber.cliente', 'dniCliente', "Cliente")
