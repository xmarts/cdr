# -*- coding: utf-8 -*-

import logging

from odoo import models, fields, api

_logger = logging.getLogger(__name__)

class Cdr(models.Model):
    _name = "sale.cdr"
    _description = "CDR for telephony records"
    #nombre = fields.Char(string="Nombre")
    numeroa= fields.Char(string="Número A",help="Número A con 10 digitos",required=True)
    numerob= fields.Char(string="Número B",help="Número B con 10 digitos")
    poblacion= fields.Char(string="Poblacion Destino",help="Población Destino")
    fecha= fields.Date(string="Fecha Llamada",help="Fecha de realización de llamada")
    inicio=fields.Datetime(string="Inicio",help="Hora de inicio de llamda")
    fin=fields.Datetime(string="Fin",help="Hora de termino de la llamada")
    min=fields.Integer(string="Min",help="Duracción de la llamada en minutos")
    montobase=fields.Float(string="Monto Base",help="Precio base")
    montofinal=fields.Float(string="Monto Final",help="Precio base")
    tarifabase=fields.Float(string="Tarifa Base",help="Tarifa Base por minuto")
    tipotrafico=fields.Selection([('CELULAR','CELULAR'),('DESCONOCIDOS','DESCONOCIDOS'),('LARGA DISTANCIA','LARGA DISTANCIA'),('LOCAL','LOCAL')],
                                 string="Tipo Trafico",help="Tipo Trafico")
    tipoorigen=fields.Char(string="Tipo Tel Origen",help="Tipo de Telefono Origen")
    tipodestino=fields.Selection([('800 INTERNACIONAL','800 INTERNACIONAL'),('800 NACIONAL','800 NACIONAL'),('LD INTERNACIONAL','LD INTERNACIONAL'),
                                   ('LD INTERNACIONAL CELULAR','LD INTERNACIONAL CELULAR'),
                                   ('LD NACIONAL','LD NACIONAL'),('LD NACIONAL CELULAR','LD NACIONAL CELULAR')],
                                string="Tipo Tel Destino",help="Tipo de  Telefono Destino")
    producto=fields.Char(string="Producto",help="Producto Ofertado")
    plan=fields.Char(string="Plan",help="Plan Ofertado")
    razonsocial=fields.Char(string="Razón Social",help="Razón Social")

