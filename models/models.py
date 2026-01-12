# -*- coding: utf-8 -*-

from odoo import models, fields, api


class NexusGreenWaterMark(models.Model):
    _inherit = 'purchase.order'

    
    # Related field to access company logo
    company_logo = fields.Binary(
        related='company_id.logo', string="Company Logo", readonly=True)

   
