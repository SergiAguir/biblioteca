# -*- coding: utf-8 -*-

from odoo import models, fields, api


class premio_model(models.Model):
    _name = 'biblioteca.premio_model'
    _description = 'Modelo de premio'
    _sql_constraints = [("sql_check_name_premio", "UNIQUE(name)","Error en el premio. El premio ya existe!"), ]

    name = fields.Char(string="Nombre",required=True,help="Nombre del genero")
    cod_autor = fields.Many2one("biblioteca.autor_model")
    cod_libro = fields.Many2one("biblioteca.libro_model")