from odoo import api, fields, models, exceptions
import logging
from . import user

class Student(models.Model):
    _name = 'dissertation_admission.student'
    _inherits = {'res.users': 'user_id'}
    _description = 'Estudante'
    user_id = fields.Many2one('res.users', ondelete='restrict')
    university_id = fields.Char(required=True)
    course = fields.Many2one('dissertation_admission.course', required=True)

    @api.model
    def create(self, values):
        user.dissertation_user_create(self.env, values)
        res = super(Student, self).create(values)
        user.recalculate_permissions(self.env, self.env['res.users'].browse(values['user_id']), 'student')
        return res

    def write(self, vals):
        return super(Student, self).write(vals)

    def unlink(self):
        user.recalculate_permissions(self.env, self.user_id, None)
        return super(Student, self).unlink()
