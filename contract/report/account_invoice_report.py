# Copyright 2021 Tecnativa - Víctor Martínez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class AccountInvoiceReport(models.Model):
    _inherit = "account.invoice.report"

    contract_id = fields.Many2one(
        "contract.contract", string="Contrato", index=True)

    def _select(self):
        select_str = super()._select()
        return "%s, line.contract_id AS contract_id" % select_str

    def _group_by(self):
        res = super()._group_by()
        return "%s, line.contract_id" % res
