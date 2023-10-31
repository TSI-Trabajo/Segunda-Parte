from odoo import models, fields, api


class Servicio(models.Model):
    _name = 'upobarber.servicio'
    _description = 'Servicio en UpoBarber'

    tiempo = fields.Char(string = "Tiempo", size = 60, required = True, help ="Duracion del servicio")
    precio = fields.Char(string = "Precio", size = 60, required = True, help ="Precio del servicio")
    

