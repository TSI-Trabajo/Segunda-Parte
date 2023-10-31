from odoo import models, fields, api


class Cita(models.Model):
     _name = 'upobarber.cita'
     _description = 'Citas de la peluqueria'

     id_cita = fields.Integer (string="ID de la Cita")
     confirmada = fields.Boolean(string="¿Cita Confirmada?", default=True)
     pagado = fields.Boolean(string="¿Pagado?", default=False)

     dni_Cliente = fields.One2many("upobarber.cliente",'cita_id','Cliente')
     reserva_id =  fields.One2many("upobarber.reserva",'cita_id','Reserva')
     horario_id = fields.Many2one("upobarber.horario",string="Horario")
     #pago_id  = fields.One2one ("upobarber.pago",'Pago')
     #reseña_id = fields.One2one ("upobarber.reseña",'Reseña')
     #nombre_Servicio = fields.Many2one ("Upobarber.servicio",stirng = " Nombre del Servicio")
     
     
     