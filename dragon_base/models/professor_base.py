from odoo import api, fields, models

class ProfessorBase(models.Model):
    _inherit = 'res.partner'

     # Add news fields
    nif = fields.Date(string='NIF')
    stat = fields.Date(string='STAT')
    rcs = fields.Date(string='RCS')
