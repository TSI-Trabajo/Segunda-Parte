# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetodoPago(models.Model):
    _name = 'upobarber.metodopago'
    _description = 'upobarber MetodoPago'

    metodo = fields.boolean(string="Metodo Pago", required=True, help="Metodo del Pago")

    #pago_id = fields.Many2One("upobarber.pago", string="Pago")