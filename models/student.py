from odoo import api, fields, models

class SchoolStudent(models.Model):
    _name = 'school.student'
    _description = 'module for manage student'
    _rec_name = 'name'


    name = fields.Char('Sudent Name')
    nik = fields.Char('NIK')
    date_birth= fields.Date('Darth of Birth')
    student_age = fields.Integer('Student Age')