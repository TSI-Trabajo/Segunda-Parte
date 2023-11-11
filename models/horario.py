from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'horario'

     name = fields.Integer(string="ID del horario", required=True, index=True)
     
     horarioInicio = fields.Datetime(required=True)
     horarioFin = fields.Datetime(required=True)
     disponible = fields.Boolean(string="¿Disponible?")

     empleado_dnis = fields.One2many("upobarber.empleado","horario_id","empleado")
     cita_ids = fields.One2many("upobarber.cita","horario_id", "cita")