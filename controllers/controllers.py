# -*- coding: utf-8 -*-
# from odoo import http


# class HrContract(http.Controller):
#     @http.route('/hr_contract/hr_contract/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_contract/hr_contract/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_contract.listing', {
#             'root': '/hr_contract/hr_contract',
#             'objects': http.request.env['hr_contract.hr_contract'].search([]),
#         })

#     @http.route('/hr_contract/hr_contract/objects/<model("hr_contract.hr_contract"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_contract.object', {
#             'object': obj
#         })
