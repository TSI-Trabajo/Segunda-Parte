# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pago(models.Model):
    _name = 'upobarber.pago'
    _description = 'upobarber Pago'

    idPago = fields.Integer("Id pago")
    metodo = fields.boolean(string="Metodo Pago", required=True, help="Metodo del Pago")
    importe = fields.Float("Importe total del pago")
    pagado = fields.boolean("Pagado")
