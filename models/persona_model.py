# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class persona_model(models.Model):
    _name = 'biblioteca.persona_model'
    _description = 'Modelo de persona'
    _sql_constraints = [("sql_check_dni_persona", "UNIQUE(dni)","Error en la persona. El dni ya existe!"), ]

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

    
    def check_DNI(self, dni):
        if len(self.dni)!=9:
            raise ValidationError("El DNI debe tener 9 caracteres")
        else:
            try:
                n=int(self.dni[:-1])
            except ValueError:
                raise ValidationError("Los primeros 8 dígitos deben ser números")

            palabra='TRWAGMYFPDXBNJZSQVHLCKE'

            if self.dni[-1].upper() == palabra[n%23]:
                return True
            else:
                
                raise ValidationError("La letra no coincide con el DNI")

    @api.constrains("email")
    def _comprobarEmail(self):
        if len(self.email)>5:
            if "@" not in self.email:
                raise ValidationError("El email tiene que contener una @")
        else:
            raise ValidationError("El email tiene que tener mas de 5 caracteres")