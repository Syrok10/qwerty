# -*- coding: utf-8 -*-

from odoo import models, fields, api

#
# class module(models.Model):
#     _name = 'module.module'
#
#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100

class Partner(models.Model):
    _inherit = 'res.partner'

    test_field = fields.Text('My New field')
    test_field1 = fields.Text('My New field1')
    test_field2 = fields.Text('My New field2')
