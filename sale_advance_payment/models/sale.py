# -*- coding: utf-8 -*-

from odoo import fields, models, _


class SaleOrder(models.Model):
    _inherit = 'sale.order'

    payment_history_ids = fields.One2many('advance.payment.history', 'order_id', string="Advanvce Payment Information")

    def set_sale_advance_payment(self):
        view_id = self.env.ref('sale_advance_payment.sale_advance_payment_wizard')

        pay_wiz_data = {
            'name': _('Sale Advance Payment'),
            'type': 'ir.actions.act_window',
            'view_type': 'form',
            'view_mode': 'form',
            'res_model': 'sale.advance.payment',
            'view_id': view_id.id,
            'target': 'new',
            'context': {
                'name': self.name,
                'order_id': self.id,
                'total_amount': self.amount_total,
                'company_id': self.company_id.id,
                'currency_id': self.currency_id.id,
                'date_order': self.date_order,
                'partner_id': self.partner_id.id,
            },
        }
        return pay_wiz_data


class AdvancePaymentHistory(models.Model):
    _name = 'advance.payment.history'
    _description = 'advance.payment.history'

    name = fields.Char(string="Name", readonly=True)
    order_id = fields.Many2one('sale.order', string="Sale Order")
    journal_id = fields.Many2one('account.journal', string="Payment (Journal)", readonly=True)
    payment_date = fields.Datetime(string="Payment Date", readonly=True)
    total_amount = fields.Float(string="Total Amount", readonly=True)
    advance_amount = fields.Float(string="Advance Paid Amount", readonly=True)
    currency_id = fields.Many2one('res.currency', string="Payment Currency", readonly=True)
    partner_id = fields.Many2one('res.partner', string="Partner")
    payment_method_id = fields.Many2one('account.payment.method', string="Payment Method", readonly=True)
