__author__ = 'wt'
import openerp.http
from openerp.http import request
from base import odootask_qweb_render
import math


class AboutController(openerp.http.Controller):
    @openerp.http.route("/about", type='http', auth="public")
    def index(self):
        context = dict()

        context["main_nav_about_active"] = True
        context["login_redirect"] = "/about"

        return odootask_qweb_render.render("odootask.about", context=context)
