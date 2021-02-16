# -*- coding: utf-8 -*-

from odoo import models, fields, api


class autor_model(models.Model):
    _name = 'biblioteca.autor_model'
    _description = 'Modelo de autor'
    _sql_constraints = [("sql_check_id_autor", "UNIQUE(name)","Error en el autor. El id ya existe!"), ]

    name = fields.Integer(string="Id",required=True,help="Id de autor")
    cod_persona = fields.One2many("biblioteca.persona_model","cod_autor")
    cod_libro = fields.One2many("biblioteca.libro_model","cod_autor")
    cod_premio = fields.One2many("biblioteca.premio_model","cod_autor")