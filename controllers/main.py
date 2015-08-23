import openerp
from base import odootask_qweb_render
from openerp.http import request
import werkzeug.utils


class Home(openerp.addons.web.controllers.main.Home):
    @openerp.http.route('/', type='http', auth="public")  # ,
    def index(self):
        return odootask_qweb_render.render("odootask.index", context={"login_redirect": "/"})

    # @openerp.http.route(auth="none")
    # def web_login(self, redirect=None, *args, **kw):
    #     r = super(Home, self).web_login(redirect=redirect, *args, **kw)
    #     if request.params['login_success'] and not redirect:
    #         if request.registry['res.users'].has_group(request.cr, request.uid, 'base.group_user'):
    #             redirect = '/web?' + request.httprequest.query_string
    #         else:
    #             redirect = '/'
    #         return openerp.http.redirect_with_hash(redirect)
    #     return r

    @openerp.http.route("/web/logout", auth="none")
    def web_logout(self):
        request.session.logout(keep_db=True)
        return werkzeug.utils.redirect("/", 303)
