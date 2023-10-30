# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    compra_id = fields.Integer("idCompra")
    importe = fields.Float("Importe")
    fechaCompra = fields.Datetime('FechaCompra')

    pago_id = fields.One2One("upobarber.pago", 'Pago')
    dniCliente = fields.One2Many("upobarber.cliente", 'compra_id', 'Cliente')
