# -*- coding: utf-8 -*-

from odoo import models, fields, api


#Al ser el Articulo un Producto que tengo en stock, para que aparezca en la vista de odoo todos los campos tengo
#que declarar todos sus atributos, pero en teoría solo con tener el id del producto y el stock serviría?

class Articulo(models.Model):
     _name = 'upobarber.articulo'
     _description = 'Articulos de UpoBarber'

     name = fields.Char(string="Nombre Articulo", size=60, required=True, help="Nombre del articulo")
     marca = fields.Char(string="Marca", size=60, required=True, help="Marca del articulo")
     modelo = fields.Char(string="Modelo", size=60, required=True, help="Modelo del articulo")
     precio = fields.Float(string="Precio", help="Precio del articulo")
     stock = fields.Integer(string="Stock")
     photo = fields.Binary('Photo')

     producto_id = fields.Many2one("upobarber.producto",string="Productos", required=True)    #FK a producto