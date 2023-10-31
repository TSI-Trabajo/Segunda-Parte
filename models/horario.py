from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'horario'

     horario_id = fields.Integer(string="ID del horario", required=True, index=True)
     
     horarioInicio = fields.Datetime(required=True)
     horarioFin = fields.Datetime(required=True)
     fecha = fields.Date(required=True)
     disponible = fields.Boolean(string="¿Disponible?")

     dniEmpleado = fields.One2many("upobarber.empleado","horario_id","empleado")
     id_cita = fields.One2many("upobarber.cita","horario_id", "cita")