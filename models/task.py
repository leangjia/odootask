from openerp import models, fields, api


# odootask.task
class Task(models.Model):
    _name = "odootask.task"

    name = fields.Char()
    close_date = fields.Date()
    description = fields.Html()

    category_id = fields.Many2one("odootask.task_category")
    comment_ids = fields.One2many("odootask.task_comment", "task_id")
    applier_ids = fields.Many2many("res.users")
    state = fields.Selection([("draft", "Draft"), ("confirmed", "Donfirmed"), ("dealed", "Dealed"), ("done", "Done"),
                              ("cancel", "Cancelled")], default="draft")

    @api.one
    def apply(self, applier_id):
        self.write({"applier_ids": [(4, applier_id, 0)]})
        # user = self.env["res.user"].sudo().search("id","=",applier_id)


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
