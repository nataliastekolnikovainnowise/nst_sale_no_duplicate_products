from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = "sale.order"

    used_product_ids = fields.Many2many(
        "product.product",
        compute="_compute_used_product_ids",
        string="Used Product Variants",
        store=False
    )

    used_product_templates = fields.Many2many(
        "product.template",
        compute="_compute_used_product_templates",
        string="Used Product Templates",
        store=False
    )

    @api.depends("order_line.product_id")
    def _compute_used_product_ids(self):
        for order in self:
            order.used_product_ids = order.order_line.mapped("product_id")

    @api.depends("order_line.product_template_id")
    def _compute_used_product_templates(self):
        for order in self:
            order.used_product_templates = order.order_line.mapped("product_template_id")
