__author__ = 'wt'
import openerp.http
from openerp.http import request
from base import odootask_qweb_render
import math


class TeamController(openerp.http.Controller):
    @openerp.http.route("/teams", type='http', auth="public")
    def index(self, **kwargs):
        context = dict()

        context["main_nav_team_active"] = True
        context["login_redirect"] = "/teams"

        return odootask_qweb_render.render("odootask.teams", context=context)
