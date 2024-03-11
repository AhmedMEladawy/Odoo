from odoo import models, fields


class AddLog(models.TransientModel):
    _name = 'log.wizard'
    _description = 'Add Log History'

    patient_id = fields.Many2one('hms.patient')
    log_id = fields.Many2one('hms.patient.line')
    description = fields.Text(required=True)

    def action_add_log(self):
       self.env['hms.patient.line'].create({
           'patient_id': self.patient_id.id,
           'description': self.description
       })