from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'Horario'
     
     horaInicio = fields.Datetime()
     horaFIn = fields.Datetime()
     fecha = fields.Date()
     disponible = fields.Boolean()

     id_Cita = fields.One2many('upobarber.cita','id_horario','Citas')
     dni_Empleado = fields.One2many("upobarber.empleado",'id_horario','Empleados')