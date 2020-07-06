# -*- coding: utf-8 -*-
from datetime import datetime

from dateutil.relativedelta import relativedelta

from odoo import models, fields, api


class HrContract(models.Model):
    _inherit = 'hr.contract'
    _description = 'Hr Contract'

    contract_file = fields.Many2many('ir.attachment', string='Contract File')
    contract_period = fields.Char(string='Contract Period (Months)', compute='_calculate_contract_time', store=True)

    @api.depends('date_start')
    def _calculate_contract_time(self):
        current_date = datetime.today().date()
        for rec in self:
            rd = relativedelta(current_date, rec.date_start)
            if rd.months == 0:
                rec.contract_period = 'Less than 1 month'
            else:
                rec.contract_period = str(rd.months)

    @api.model
    def _send_notify(self):
        search_month = self.env['hr.contract'].search([
            ('state', 'in', ['open']), ('contract_period', '=', 6)
        ])
        group_admin = self.env.ref('hr_contract_inherit.group_employee_manager')
        list_user = []
        if group_admin:
            if group_admin.users:
                for user in group_admin.users:
                    if user:
                        list_user.append(user.partner_id.id)
        if search_month:
            for rec in search_month:
                if rec:
                    rec.message_post(body="The employee's contract upto the time of evaluation. Please check!",
                                     message_type="notification", partner_ids=list_user)
