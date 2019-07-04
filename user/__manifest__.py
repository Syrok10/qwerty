# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Signup',
    'description': """
Allow users to sign up and reset their password
===============================================
    """,
    'version': '1.0',
    'category': 'Extra Tools',
    'auto_install': True,
    'depends': [
        'base_setup',
        'mail',
        'web',
    ],
    'data': [

        'views/auth_signup_login_templates.xml',

    ],
    'bootstrap': True,
}