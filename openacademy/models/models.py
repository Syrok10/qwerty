# -*- coding: utf-8 -*-

from odoo import models, fields, api


class openacademy(models.Model):
    _name = 'openacademy.course'
    _description = 'openacademy course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('res.user',
                                     ondelete='set null', string="Responsible", index=True)


class Session(models.Model):
    _name = 'openacademy.session'
    _description = "Openacademy Sessions"

    name = fields.Char(required=True)
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
