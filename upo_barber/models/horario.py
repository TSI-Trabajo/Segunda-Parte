from odoo import models, fields, api


class Horario(models.Model):
     _name = 'upobarber.horario'
     _description = 'Horario'
     
     horaFIn = fields.Char(string="Hora de finalizacion", size=9, required=True)

     id_Cita = fields.One2many('upobarber.cita','id_horario','Citas')
     dni_Empleado = fields.One2many("upobarber.empleado",'id_horario','Empleados')