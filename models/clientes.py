from odoo import models, fields, api


class Clientes(models.Model):
     _name = 'peluqueria.clientes'
     _description = 'Clientes de la peluquería.'

     name = fields.Char(string="Title", required=True, help="Nombre del cliente")
     apellidos = fields.Char(string="Title", required=True, help="Apellidos del cliente")
     telefono  = fields.Integer()
     dni = fields.Char()
     correoElectronico = fields.Char(string="Title", required=True, help="Correo Electronico del cliente")
     
     
     citas_ids = fields.Many2one("peluqueria.citas",string="Confirmar cita")
     
     
