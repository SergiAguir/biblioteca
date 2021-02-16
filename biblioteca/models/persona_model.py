# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class persona_model(models.Model):
    _name = 'biblioteca.persona_model'
    _description = 'Modelo de persona'
    _sql_constraints = [("sql_check_dni_persona", "UNIQUE(name)","Error en la persona. El dni ya existe!"), ]

    name = fields.Char(string="Nombre", required=True,help="Nombre de la persona")
    apellidos = fields.Char(string="Apellidos", required=True, help="Apellidos de la persona")
    dni = fields.Char(string="DNI", required=True, help="DNI de la persona")
    telf = fields.Integer(string="Telefono", size=9,required=True,help="Telefono de la persona")
    email = fields.Char(string="Email", size=50,required=True, help="Email de la persona")
    foto = fields.Binary()
    edad = fields.Integer(string="Edad", required=True,help="Edad de la persona")
    localidad = fields.Char(string="Localidad", required=True, help="Localidad de la persona")
    cod_socio = fields.Many2one("biblioteca.socio_model")
    cod_bibliotecario = fields.Many2one("biblioteca.bibliotecario_model")
    cod_autor = fields.Many2one("biblioteca.autor_model")


    def check_DNI(self, ndni):
        tabla = "TRWAGMYFPDXBNJZSQVHLCKE"
        dig_ext = "XYZ"
        reemp_dig_ext = {'X': '0', 'Y': '1', 'Z': '2'}
        numeros = "1234567890"
        dni = ndni.upper()
        if len(dni) == 9:
            dig_control = dni[8]
            dni = dni[:8]
            if dni[0] in dig_ext:
                dni = dni.replace(dni[0], reemp_dig_ext[dni[0]])
            return len(dni) == len([n for n in dni if n in numeros]) \
                and tabla[int(dni) % 23] == dig_control
        return False
