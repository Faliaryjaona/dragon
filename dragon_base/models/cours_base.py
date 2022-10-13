from odoo import api, fields, models

class CoursBase(models.Model):
    _name = 'cours.base'
    _description = 'cours_base'

    name = fields.Char(string="Name")
    matiere = fields.Char(string="Matiere")
    professor = fields.Char(string="Professor")
    niveau = fields.Selection([
        ('l1', 'L1'),
        ('l2', 'L2'),
        ('l3', 'L3'),
        ('m1', 'M1'),
        ('m2', 'M2'),
    ], default='l1', string="Niv")
    class_cours = fields.Char(string="Salle de cours")



