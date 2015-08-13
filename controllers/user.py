__author__ = 'wt'
import openerp.http
from openerp.http import request
from base import odootask_qweb_render
import math


class UserController(openerp.http.Controller):
    @openerp.http.route(["/user", "/user/<int:user_id>"], type='http', auth="user", method=["GET"])
    def index(self, user_id=None):
        if not user_id:
            user = request.env.user
        else:
            user = request.env["res.users"].sudo().search([("id", "=", user_id)])

        context = dict()
        context["login_redirect"] = "/user"

        context["user"] = user
        context["is_myself"] = not user_id

        return odootask_qweb_render.render("odootask.user", context=context)
