# -*- coding: utf-8 -*-

from odoo import models, fields


class LibraryAuthor(models.Model):
    _name = "library.author"
    _description = "Authors"

    name = fields.Char(string="Full Name")
    address = fields.Text(string="Address")
