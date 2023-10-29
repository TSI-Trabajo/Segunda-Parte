from odoo import models, fields, api


class Empleado(models.Model):
     _name = 'upobarber.empleado'
     _description = 'Empleados'

     nombre = fields.Char(string="Nombre", size=60, required=True, help="Nombre del empleado")
     apellidos = fields.Char(string="Apellidos", size=60, required=True, help="Apellidos del empleado")
     telefono = fields.Integer(string="Telefono", size=10, required=True, help="Telefono del Empleado")
     correoElectronico = fields.Char(string="Correo Electronico", size=50, required=True, help="Correo electronico del Empleado")
     numeroCuenta = fields.Char(string="NUmero de Cuenta", size=50, required=True, help="Numero de cuenta del empleado")
     
     id_Horario = fields.Many2one("upobarber.horario",string="Horario")