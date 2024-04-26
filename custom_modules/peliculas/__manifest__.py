# -*- coding:utf-8 -*-

{
    # Nombre del Modulo
    'name': 'Modulo de peliculas',
    # Version del Modulo
    'version': '1.0',
    # Dependencias: Permite al modulo ser creado
    'depends': [
        'contacts',
    ],
    # Autor del Modulo
    'author': 'Martin Urisman',
    # Categorias a utilizar de Odoo
    'category': 'Peliculas',
    # URL Web
    'website': 'https://www.google.cl',
    # Descripcion
    'summary': 'Modulo de presupuestos',
    # Descripcion del Modulo (HTML)
    'description': '''
        Modulo para hacer presupuesto de peliculas
    ''',
    # Data: archivos '.XML' y '.CSV' que se crean dentro del modelo
    'data': [
        'views/menu.xml',
        'views/presupuesto_views.xml',
    ],
}