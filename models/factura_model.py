# -*- coding: utf-8 -*-

from odoo import models, fields, api
from datetime import datetime,date

class factura_model(models.Model):
    _name = 'biblioteca.factura_model'
    _description = 'Modelo de factura'
    _sql_constraints = [("sql_check_name_factura", "UNIQUE(name)","Error en la factura. La referencia ya existe!"), ]


    name= fields.Integer(string="Referencia",help="Referencia de la Factura")
    fecha= fields.Date(string="Fecha", default=lambda self: datetime.today())
    cod_socio = fields.Many2one("biblioteca.socio_model",string="Socio")
    cod_dfacturas = fields.One2many("biblioteca.dfacturas_model","cod_factura",string="Factura")
    base = fields.Float(string="Base", compute="_calc_base", store=True)
    iva = fields.Selection(string="IVA", default='21', selection=[('21','21'),('15', '15'),('7', '7'),('0', '0')], required=True)
    total = fields.Float(string="Total", compute="_calc_iva", store=True)
    

    @api.depends('cod_dfacturas')
    def _calc_base(self):
        self.ensure_one()
        suma = 0
        for i in self.cod_dfacturas:
            suma += i.cod_libro.precio*i.cantidad
        self.base = suma

    @api.depends('iva', 'base')
    def _calc_iva(self):
        self.ensure_one()
        self.total = (((self.base*int(self.iva))/100)+self.base)