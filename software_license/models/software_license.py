# -*- coding: utf-8 -*-
# Copyright (C) DEC SARL, Inc - All Rights Reserved.
# Written by Yann Papouin <ypa at decgroupe.com>, Mar 2020

from odoo import _, api, fields, models


class SoftwareLicense(models.Model):
    _name = 'software.license'
    _description = 'License'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'serial'
    _order = 'id desc'

    @api.model
    def _get_default_serial(self):
        if self.env.context.get('default_type') == 'template':
            new_id = self.search([], order='id desc', limit=1).id + 1
            return _('✳️ Template %d') % (new_id)
        else:
            return _('New')

    active = fields.Boolean(
        'Active',
        default=True,
        help="If unchecked, it will allow you to hide the license "
        "without removing it.",
    )
    serial = fields.Char(
        required=True,
        copy=False,
        default=_get_default_serial,
        track_visibility='onchange',
        help="Unique serial used as an authorization identifier",
    )
    application_id = fields.Many2one(
        'software.license.application',
        'Application',
        required=True,
    )
    hardware_ids = fields.One2many(
        comodel_name='software.license.hardware',
        inverse_name='license_id',
        string="Hardware Identifiers",
        copy=False,
        help="Unique hardware identifiers sent by client application made to "
        "identify a system. This identifier must not change over time or "
        "activation related data would be invalidated"
    )
    product_id = fields.Many2one(
        'product.product',
        'Product',
        domain=[],
        change_default=True,
    )
    production_id = fields.Many2one('mrp.production', 'Production')
    partner_id = fields.Many2one('res.partner', 'Partner')
    info = fields.Text('Informations')
    type = fields.Selection(
        selection=[
            ('normal', _('Normal')),
            ('template', _('Template')),
        ],
        string='Type',
        default='normal',
        required=True
    )

    _sql_constraints = [
        (
            'serial_uniq', 'unique(serial,application_id)',
            'Serial Activation Code must be unique per Application!'
        ),
    ]

    @api.multi
    @api.returns('self', lambda value: value.id)
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        if not default.get('serial'):
            default.update(serial=_('%s (copy)') % (self.serial))
        return super(SoftwareLicense, self).copy(default)

    def _name_get(self):
        self.ensure_one()
        return ('[%s] %s') % (self.application_id.name, self.serial)

    @api.multi
    @api.depends('serial', 'application_id.name')
    def name_get(self):
        result = []
        for rec in self:
            name = rec._name_get()
            result.append((rec.id, name))
        return result

    def _prepare_hardware_activation_vals(self, hardware):
        res = {
            'license_id': self.id,
            'name': hardware,
        }
        return res

    @api.multi
    def activate(self, hardware, params=False):
        self.ensure_one()
        vals = self._prepare_hardware_activation_vals(hardware)
        return self.env['software.license.hardware'].create(vals)
