# -*- coding: utf-8 -*-

from odoo import models, fields, api

class tiposervicio(models.Model):
    _name = 'upobarber.tiposervicio'
    _description = 'Tipo de Servicio'

    
    tipo_servicio = fields.Char(string="Tipo Servicio", required=True, index=True)
    descripción = fields.Char(string="Descripción", required=True)

    