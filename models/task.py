from openerp import models, fields, api, _


# odootask.task
class Task(models.Model):
    _inherit = "mail.thread"
    _name = "odootask.task"

    name = fields.Char()

    close_date = fields.Date()
    description = fields.Text()

    category_id = fields.Many2one("odootask.task_category")
    comment_ids = fields.One2many("odootask.task_comment", "task_id")
    applier_ids = fields.Many2many("res.users")
    state = fields.Selection(
        [("draft", "Draft"), ("confirmed", "Confirmed"), ("approved", "Approved"), ("applying", "Applying"),
         ("applied", "Applied"), ("done", "Done"), ("cancel", "Cancelled")], default="draft")

    @api.one
    def apply(self, applier_id):
        self.write({"applier_ids": [(4, applier_id, 0)]})

    @api.one
    def approve(self):
        self.state = "approved"
        self.message_post(body=_("Approved by %s") % self.env.user.name)

    @api.one
    def draft(self, reason=""):
        self.state = "draft"
        self.message_post(body=_("Refused,reason:%s") % reason)

    @api.one
    def applying(self):
        self.state = "applying"


# odootask.task_category
class TaskCategory(models.Model):
    _name = "odootask.task_category"

    name = fields.Char()
    task_ids = fields.One2many("odootask.task", "category_id")


# odootask.task_comment
class Comment(models.Model):
    _name = "odootask.task_comment"
    content = fields.Char(size=1000)
    task_id = fields.Many2one("odootask.task")


class User(models.Model):
    _inherit = "res.users"

    odootask_ids = fields.One2many("odootask.task", "create_uid")
