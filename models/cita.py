from odoo import models, fields, api


class Cita(models.Model):
     _name = 'upobarber.cita'
     _description = 'Citas'

     horaInicio = fields.Datetime()
     horaFin = fields.Datetime()
     fecha = fields.Date()

     id_Horario = fields.Many2one("upobarber.horario",string="Horario")