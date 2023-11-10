# -*- coding: utf-8 -*-

from odoo import models, fields, api


class resena(models.Model):
    _name = 'upobarber.resena'
    _description = 'resenas Upobarber'
    
    resena_id = fields.Char(string="ID de la resena")
    puntuacion = fields.Integer(string="puntuacion de la resena", required=True)
    comentarios = fields.Char(string="Comentarios", required=True)

