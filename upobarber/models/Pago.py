# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Pago(models.Model):
    _name = 'upobarber.pago'
    _description = 'upobarber Pago'

    _rec_name = 'name'

    name = fields.Integer(string="Id pago", required=True)
    #importe = fields.Float(string="Importe total del pago")
    pagado = fields.Boolean(string="Pagado", default=False)
    concepto = fields.Char(string="Concepto del pago", required=True)

    metodo_id = fields.Many2one('upobarber.metodopago',string="Metodo Pago")
    #cita_id = fields.related('upobarber.Cita', string="Cita")
    compra_id = fields.Many2one('upobarber.compra', string="Compra")

