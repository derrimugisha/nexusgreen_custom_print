# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NexusResUser(models.Model):
    _inherit = 'res.users'

    user_signature = fields.Html(string='User Signature', sanitize=False)
    user_signature_image = fields.Binary(
        string='Signature Image', attachment=True)


class HrEmployee(models.Model):
    _inherit = 'hr.employee'

    user_signature = fields.Html(
        related='user_id.user_signature',
        string='User Signature',
        readonly=False,
    )


class HrEmployeePublic(models.Model):
    _inherit = 'hr.employee.public'

    user_signature = fields.Html(
        related='user_id.user_signature',
        string='User Signature',
        readonly=False,
    )


class NexusGreenWaterMark(models.Model):
    _inherit = 'purchase.order'

    company_logo = fields.Binary(
        related='company_id.logo', string="Company Logo", readonly=True)
    checked_by = fields.Many2one("res.users", string="Checked by")
    confirmed_by = fields.Many2one("res.users", string="Authorized by")
    approval_by = fields.Many2one("res.users", string="Appraver ")

    def button_confirm(self):
        res = super().button_confirm()
        self.confirmed_by = self.env.user
        return res
