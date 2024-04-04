# -*- coding: utf-8 -*-
# from odoo import http


# class NexusgreenCustomPrint(http.Controller):
#     @http.route('/nexusgreen_custom_print/nexusgreen_custom_print/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/nexusgreen_custom_print/nexusgreen_custom_print/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('nexusgreen_custom_print.listing', {
#             'root': '/nexusgreen_custom_print/nexusgreen_custom_print',
#             'objects': http.request.env['nexusgreen_custom_print.nexusgreen_custom_print'].search([]),
#         })

#     @http.route('/nexusgreen_custom_print/nexusgreen_custom_print/objects/<model("nexusgreen_custom_print.nexusgreen_custom_print"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('nexusgreen_custom_print.object', {
#             'object': obj
#         })
