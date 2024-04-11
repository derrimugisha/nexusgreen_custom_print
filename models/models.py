# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class nexusgreen_custom_print(models.Model):
#     _name = 'nexusgreen_custom_print.nexusgreen_custom_print'
#     _description = 'nexusgreen_custom_print.nexusgreen_custom_print'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class NexusGreenWaterMark(models.Model):
    _inherit = 'purchase.order'

    # Add a field to connect to res.company
    company_id = fields.Many2one('res.company', string='Company')

    # Related field to access company logo
    company_logo = fields.Binary(
        related='company_id.logo', string="Company Logo", readonly=True)

    @api.model
    def create(self, vals):
        if not vals.get('company_id'):
            vals['company_id'] = self.env.company.id
            print("@@@@@@"*12)
            print(vals)
            print("@@@@@@"*12)
        return super(NexusGreenWaterMark, self).create(vals)
