# -*- coding:utf-8 -*-

import logging

from odoo import fields, models, api
from odoo.exceptions import UserError


logger = logging.getLogger(__name__)

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

    puntuacion = fields.Integer(string='Puntuación', related='puntuacion_change') # Puntuacion de la Pelicula

    puntuacion_change = fields.Integer(string='Editar puntuación')

    active = fields.Boolean(string='Activo', default=True) # Campo reservado Odoo para realizar un borrado logico (no se borra de la db)

    director_id = fields.Many2one(string='Director', comodel_name='res.partner') # Campo ID del director

    categoria_director_id = fields.Many2one(
        comodel_name='res.partner.category',
        string='Categoria Director',
        # Al crear una pelicula, se asigna la categoria Director por default!, esto lo hace con la funcion lambda
        default=lambda self: self.env['res.partner.category'].search([('name', '=', 'Director')])
    )

    genero_ids = fields.Many2many(string='Generos', comodel_name='genero') # Campo ID's de generos

    vista_general = fields.Text(string='Descripcion') # Campo descripcion de la pelicula

    link_trailer = fields.Char(string='Trailer') # Campo link trailer de la pelicula

    es_libro = fields.Boolean(string='Version Libro') # Campo si existe version libro de la pelicula

    libro = fields.Binary(string='Libro') # Campo libro PDF

    libro_filename = fields.Char(string='Nombre del Libro')

    # Estado del registro (Borrador, Aprobado, Cancelado, etc..)
    # Parametro copy: Permite que al copiar un registro este no copie el estado actual del registro copiado, es decir, lo dejara en borrador por default
    state = fields.Selection(
        selection=[
            ('Borrador', 'Borrador'),
            ('Aprobado', 'Aprobado'),
            ('Cancelado', 'Cancelado'),
        ], default='Borrador', string='Estados', copy=False
    )

    fecha_aprobado = fields.Datetime(string="Fecha Aprobado", copy=False)

    
    def aprobar_presupuesto(self):
        # Logger personalizado
        logger.info('[+] Presupuesto aprobado!')
        self.state = 'Aprobado'
        self.fecha_aprobado = fields.Datetime.now()
    
    def cancelar_presupuesto(self):
        # Logger personalizado
        logger.warning('[*] Presupuesto cancelado!')
        self.state = 'Cancelado'
    
    # Definicion de la funcion unlink
    def unlink(self):
        logger.info('[!] Se disparo la funcion unlink')
        
        if self.state != 'Cancelado':
            raise UserError('[ERROR] No se pudo eliminar el registro, no se encuentra en estado "Cancelado"')
        # Llamado a la funcion unlink (eliminar) original
        super(Presupuesto, self).unlink()
    
    # Definicion de la funcion unlink
    @api.model # Decorador para al funcion create
    def create(self, variables):
        logger.info('[+] Variables: {0}'.format(variables))
        # Retornando la funcion create (crear) original
        return super(Presupuesto, self).create(variables)