# -*- coding:utf-8 -*-

from odoo import fields, models, api

class Presupuesto(models.Model):

    _name = "presupuesto" # Nombre de la Tabla en la Base de Datos

    _inherit = ['image.mixin'] # Herencia del modelo de imagenes

    name = fields.Char(string='Pelicula') # Campo reservado Odoo, es el nombre del nuevo registro

    clasificacion = fields.Selection(selection=[
    #    db   view   
        ('G', 'G'), # Publico General
        ('PG', 'PG'), # Compañia de un adulto
        ('PG-13', 'PG-13'), # Mayores de 13 años
        ('R', 'R'), # Compañia de un adulto (Obligatorio)
        ('NC-16', 'NC-16'), # Mayores de 16
        ('M-18', 'M-18') # Mayores de 18
    ], string='Clasificación')

    fecha_estreno = fields.Date(string='Fecha estreno') # Fecha de estreno de la Pelicula

    puntuacion = fields.Integer(string='Puntuación') # Puntuacion de la Pelicula

    active = fields.Boolean(string='Activo', default=True) # Campo reservado Odoo para realizar un borrado logico (no se borra de la db)


    director_id = fields.Many2one(string='Director', comodel_name='res.partner') # Campo ID del director

    genero_ids = fields.Many2many(string='Generos', comodel_name='genero') # Campo ID's de generos

    vista_general = fields.Text(string='Descripcion') # Campo descripcion de la pelicula

    link_trailer = fields.Char(string='Trailer') # Campo link trailer de la pelicula

    es_libro = fields.Boolean(string='Version Libro') # Campo si existe version libro de la pelicula

    libro = fields.Binary(string='Libro') # Campo libro PDF