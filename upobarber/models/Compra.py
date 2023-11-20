# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    name = fields.Integer(string="idCompra", index=True, required=True)
    importe = fields.Float(string="Importe", required=True)
    fechaCompra = fields.Datetime(string="Fecha Compra", required=True)

    pago_id = fields.Many2one('upobarber.pago', string="Pago")
    #cliente_id = fields.One2many('upobarber.cliente', 'dniCliente', "Cliente")
