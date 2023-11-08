from odoo import models, fields, api

class Servicio(models.Model):
    _name = 'upobarber.servicio'
    _description = 'Servicios Upobarber'
        
    nombre_servicio = fields.Char(string="Nombre del servicio")
    tiempo = fields.Float(string="Tiempo", required=True)
    precio = fields.Float(string="Precio", required=True)

    tipo_servicio = fields.Many2one('upobarber.tiposervicio', string='Servicio Relacionado')
