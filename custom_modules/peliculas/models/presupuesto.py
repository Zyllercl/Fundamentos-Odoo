# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Presupuesto(models.Model):

    _name = "presupuesto" # Referencia a la clase

    name = fields.Char() # Referencia a la descripcion por defecto de la db