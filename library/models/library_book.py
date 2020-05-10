# -*- coding: utf-8 -*-

from odoo import api, models, fields, exceptions


class LibraryBook(models.Model):
    _name = "library.book"
    _description = "Books"

    name = fields.Char(
        string="Book",
        default="New Book",
        required=True,
        help="Escriba el nombre completo del libro",
        index=True)
    isbn = fields.Char(
        string="ISBN",
        required=True,
        size=30)
    description = fields.Text(
        string="Description",
        help="Escriba una descripcion sinoptica del libro")
    category_ids = fields.One2many(
        comodel_name="library.category",
        inverse_name="book_id",
        string="Categories")
    category_count = fields.Integer(
        string="Categories #",
        compute="_count_categ")
    state = fields.Selection(
        string="State",
        selection=[('bf', 'bf'),
                   ('it', 'it'),
                   ('success', 'success'),
                   ('info', 'info'),
                   ('warning', 'warning'),
                   ('danger', 'danger'),
                   ('muted', 'muted'),
                   ('primary', 'primary'),
                   ('dual', 'dual'),],
        required=True, )
    image = fields.Binary(string="Image")
    date_publish = fields.Date(string="Publish Date", required=True)
    author_id = fields.Many2one(comodel_name="library.author", string="Author", required=True)
    color = fields.Integer(string="Color", required=True)

    _sql_constraints = [
        ('isbn_book_uniq', 'unique(isbn)', """ISBN must be unique""")
    ]

    def _count_categ(self):
        for book in self:
            book.category_count = len(book.category_ids)

    @api.constrains("isbn")
    def check_isbn_unique(self):
        isbn = self.search([['id','!=', self.id]]).mapped("isbn")
        if self.isbn and self.isbn in isbn:
            raise exceptions.ValidationError("ISBN duplicado")
