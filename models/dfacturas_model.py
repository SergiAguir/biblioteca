# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class dfacturas_model(models.Model):
    _name = 'biblioteca.dfacturas_model'
    _description = 'Modelo detalle de factura'

    cod_factura = fields.Many2one("biblioteca.factura_model",string="Factura")
    cod_libro = fields.Many2one("biblioteca.libro_model",string="Libro")
    cantidad = fields.Integer(string="Cantidad",default=1,required=True)

    @api.constrains('cantidad')
    def _comprobarCant(self):
        if self.cantidad < 0:
            raise ValidationError("La minima catidad de un producto tiene que ser 1")