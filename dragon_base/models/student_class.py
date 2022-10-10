# -*- coding: utf-8 -*-

from odoo import models, fields, api


class StudentClass(models.Model):
    _name = 'student.class'
    _description = "Classes table"

    name = fields.Char(string="Name")
    class_number = fields.Integer(string="Class number")
    stage = fields.Selection([
        ('l1', 'L1'),
        ('l2', 'L2'),
        ('l3', 'L3'),
        ('m1', 'M1'),
        ('m2', 'M2'),
    ], default='l1', string="Stage")
