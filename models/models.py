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


class IsCallOffReturner(models.Model):
    _inherit = "project.project"

    call_off_order = fields.Boolean("Call Off Order", defaults=False)

    def open_call_off_orders(self):
        # form_id = self.env['ir.model.data'].get_object_reference('purchase', 'purchase_order_form')[1]
        context = dict(self._context or {})
        context['default_project_id'] = self.id
        print("")
        return {
            'name': 'Call Off Orders',
            # 'view_type': 'tree,form',
            'view_mode': 'tree,form',
            'domain': [('project_id', '=', self.id), ('call_off_order', '=', True)],
            'res_model': 'purchase.order',
            'context': context,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }

    @api.depends("call_off_orders")
    def _compute_call_off_order_no(self):
        for rec in self:
            true_count = sum(
                order.call_off_order for order in rec.call_off_orders if order.call_off_order)
            rec.call_off_order_no = true_count
