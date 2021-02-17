# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class bibliotecario_model(models.Model):
    _name = 'biblioteca.bibliotecario_model'
    _description = 'Modelo de bibliotecario'
    _sql_constraints = [("sql_check_id_bibliotecario", "UNIQUE(name)","Error en el bibliotecario. El id ya existe!"), ]

    name = fields.Integer(string="Id",required=True,help="Id de bibliotecario")
    fechaAlta = fields.Date(string="Fecha", default=lambda self: datetime.today())
    cod_persona = fields.One2many("biblioteca.persona_model","cod_bibliotecario")
    cod_prestamo = fields.One2many("biblioteca.prestamo_model","cod_bibliotecario")