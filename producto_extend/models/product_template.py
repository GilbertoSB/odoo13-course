# -*- coding: utf-8 -*-

from odoo import api, models, fields


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    typology = fields.Selection(
        string="", selection=[
            ('metal', 'Metal'),
            ('pvc', 'PVC'),
            ('cristal', 'Cristal'),
        ]
    )
