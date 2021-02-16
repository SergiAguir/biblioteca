# -*- coding: utf-8 -*-

from odoo import models, fields, api


class genero_model(models.Model):
    _name = 'biblioteca.genero_model'
    _description = 'Modelo de genero'
    _sql_constraints = [("sql_name:check", "UNIQUE(name)","Error en el genero. El genero ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre de genero")
    descripcion = fields.Html()
    cod_libro = fields.One2many("biblioteca.libro_model","cod_genero")