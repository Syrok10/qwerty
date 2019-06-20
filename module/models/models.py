# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    test_field = fields.Text('My New field')
    test_field1 = fields.Text('My New field1')
    test_field2 = fields.Text('My New field2')
