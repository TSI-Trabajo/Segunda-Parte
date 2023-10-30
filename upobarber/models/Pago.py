# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pago(models.Model):
    _name = 'upobarber.pago'
    _description = 'upobarber Pago'

    pago_id = fields.Integer("Id pago")
    importe = fields.Float("Importe total del pago")
    pagado = fields.boolean("Pagado")

    metodo = fields.One2Many("gym.metodopago", 'pago_id', 'MetodoPago')
    cita_id = fields.One2One("upobarber.cita", 'Cita')
    compra_id = fields.One2One("upobarber.compra", 'Compra')

