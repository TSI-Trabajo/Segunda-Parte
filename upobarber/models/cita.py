from odoo import models, fields, api

class Cita(models.Model):
     _name = 'upobarber.cita'
     _description = 'Citas de la peluqueria'

     name = fields.Integer(string="ID de la Cita",required=True)
     confirmada = fields.Boolean(string="¿Cita Confirmada?",default=True)
     pagado = fields.Boolean(string="¿Pagado?",default=False)

     cliente_id = fields.Many2one("upobarber.cliente",'Cliente')
     reserva_id = fields.Many2one("upobarber.reserva",'Reserva')
     #horario_id = fields.One2many("upobarber.horario",string="Horario")
     #pago_id  = fields.One2one ("upobarber.pago",'Pago')
     #reseña_id = fields.One2one ("upobarber.reseña",'Reseña')
     #nombre_Servicio = fields.Many2one ("Upobarber.servicio",stirng = " Nombre del Servicio")
     