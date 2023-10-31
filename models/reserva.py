from odoo import models, fields, api


class Reserva(models.Model):
     _name = 'upobarber.reserva'
     _description = 'Reservas de la peluquería.'

     reserva_id = fields.Char(string="IdReserva", size=60, required=True, help="Nombre del cliente")
     telefonoContacto  = fields.Integer(string="Telefono",size = 9, required=True, help = "Telefono MOVIL del peluquero")
     fechaReserva = fields.Date (string="Fecha", required=True, index=True, default=fields.Date.today())
     
     cita_id = fields.Many2one("upobarber.cita",string="Citas de la reserva")