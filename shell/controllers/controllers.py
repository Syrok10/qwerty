# -*- coding: utf-8 -*-
from odoo import http

# class Shell(http.Controller):
#     @http.route('/shell/shell/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/shell/shell/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('shell.listing', {
#             'root': '/shell/shell',
#             'objects': http.request.env['shell.shell'].search([]),
#         })

#     @http.route('/shell/shell/objects/<model("shell.shell"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('shell.object', {
#             'object': obj
#         })