# -*- coding: utf-8 -*-

from odoo import models, fields, api
import datetime
from dateutil import relativedelta


class ProductAnalyzer(models.Model):
    _name = 'product_analyzer.product_analyzer'
    _description = 'product_analyzer'

    sheet_id = fields.One2many('product_analyzer.product_analyzer.sheet', 'sheet_list')
    # value = fields.Integer()
    # value2 = fields.Float(compute="_value_pc", store=True)
    # description = fields.Text()
    start_date = fields.Date(string='Order history start date:',
                             default=datetime.date.today() - relativedelta.relativedelta(months=1))
    product_id = fields.Many2one('product.product', string='Product')

    # @api.depends('value')
    # def _value_pc(self):
    #     for record in self:
    #         record.value2 = float(record.value) / 100





class ProductAnalyzerSheet(models.Model):
    _name = 'product_analyzer.product_analyzer.sheet'
    _description = 'product_analyzer_sheet'

    sheet_list = fields.Many2one('product_analyzer.product_analyzer')
    sku = fields.Char(string='SKU')
    title = fields.Char(string='Title')
    direct = fields.Integer(string='Direct')
    replenishment = fields.Integer(string='Replenishment')
    sold = fields.Integer(string='Qty Sold')
    inventory = fields.Integer(string='Inventory')
    demand = fields.Integer(string='Demand')
    production = fields.Integer(string='Production', compute='_compute_production')
    actual_demand = fields.Integer(string='Actual Demand')
    actual_production = fields.Integer(string='Actual Production')
    completed = fields.Date(string='Completed')

    @api.depends('inventory', 'demand')
    def _compute_production(self):
        for record in self:
            record.production = record.demand - record.inventory