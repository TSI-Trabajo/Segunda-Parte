from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'horario'

     name = fields.Integer(string="ID del horario", required=True, index=True)
     
     horarioInicio = fields.Datetime(required=True)
     horarioFin = fields.Datetime(required=True)
     disponible = fields.Boolean(string="¿Disponible?")

     empleado_dnis = fields.Many2one("upobarber.empleado", string="Empleados")
     cita_ids = fields.Many2one("upobarber.cita", string="Citas")