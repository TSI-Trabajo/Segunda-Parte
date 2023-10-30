# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name = 'upobarber.compra'
    _description = 'upobarber Compra'

    #idCompra = fields.Integer("idCompra")
    #idPago = fields.Integer("idPago")
    dniCliente = fields.One2Many("res.cliente", 'Cliente', required=True)
    importe = fields.Float("Importe")
