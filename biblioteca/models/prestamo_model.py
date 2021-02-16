# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime
from time import time

class prestamo_model(models.Model):
    _name = 'biblioteca.prestamo_model'
    _description = 'Modelo de prestamo'

    name = fields.Date(string="Fecha", default=lambda self: datetime.today())
    cod_socio = fields.Many2one("biblioteca.socio_model")
    cod_libro = fields.Many2many("biblioteca.libro_model",string="Lista libro")
    cod_bibliotecario = fields.Many2one("biblioteca.bibliotecario_model")