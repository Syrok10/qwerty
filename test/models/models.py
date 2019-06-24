# -*- coding: utf-8 -*-

from odoo import models, fields, api


class test(models.Model):
    _name = 'test.course'
    _description = "Test course"

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
