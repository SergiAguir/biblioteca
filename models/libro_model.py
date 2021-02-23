# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class libro_model(models.Model):
    _name = 'biblioteca.libro_model'
    _description = 'Modelo de libro'
    _sql_constraints = [("sql_check_name_libro", "UNIQUE(name)","Error en el libro. El libro ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre del libro",index=True)
    id = fields.Integer(string="Id",required=True,help="Id del libro")
    foto = fields.Binary()
    fecha = fields.Date(string="Fecha", default=lambda self: datetime.today())
    calificacion = fields.Selection(selection=[('1', '1'),('2','2'),('3','3'),('4','4'),('5','5')])
    isbn = fields.Char(string="ISBN", requiered=True,help="Isbn del libro")
    prestado = fields.Boolean(string="Esta prestado?", default=False)
    precio = fields.Float(string="Precio",required=True,help="Precio del producto")
    cod_autor = fields.Many2one("biblioteca.autor_model")
    cod_genero = fields.Many2one("biblioteca.genero_model")
    cod_premio = fields.One2many("biblioteca.premio_model","cod_libro")
    cod_prestamo = fields.Many2many("biblioteca.prestamo_model")
    cod_dfacturas = fields.One2many("biblioteca.dfacturas_model","cod_libro")

    def cambiaEstado(self):
          self.ensure_one()
          self.prestado = not self.prestado
          return True