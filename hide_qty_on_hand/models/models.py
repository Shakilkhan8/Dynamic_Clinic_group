# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class InheritSTokcMove(models.Model):
    _inherit = 'stock.move'

    @api.onchange('product_uom_qty', )
    def check_qty_on_hand(self):
        for rec in self:
            if rec.product_id:
                if rec.product_uom_qty > rec.product_id.qty_available:
                    raise ValidationError("Demand qty can't be greater than qty on Hand")


