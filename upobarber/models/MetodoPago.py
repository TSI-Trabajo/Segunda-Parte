# -*- coding: utf-8 -*-

from odoo import models, fields, api

class MetodoPago(models.Model):
    _name = 'upobarber.metodopago'
    _description = 'upobarber MetodoPago'

    _rec_name= 'metodos'

    name = fields.Integer(string="Id del métodoPago", index=True, required=True)
    metodos = fields.Char(string="Método del Pago", required=True)
    pago_ids = fields.One2many('upobarber.pago', 'metodo_id', "Metodo Pago")

    #pago_id = fields.Many2One("upobarber.pago", string="Pago")    name = fields.Integer(string="Id pago", index=True, required=True)
