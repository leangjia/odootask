__author__ = 'wt'
import openerp.http


class OdooTaskQwebRender(object):
    def __init__(self, request):
        self.request = request

    def render(self, template, context=None):
        context = context or dict()
        context["is_login"] = False
        context['username'] = ""
        context["is_public"] = False
        context["is_website_user"] = False
        context["is_admin"] = False
        if "login_redirect" not in context:
            context['login_redirect'] = "/"

        try:
            env = openerp.http.request.env
            user = env.user
            if user and user.id:
                context["is_login"] = True
                context['username'] = env.user.name
                context["is_public"] = user == env.ref("base.public_user")
                context["is_website_user"] = user.has_group("odootask.group_odootask_user")
                context["is_admin"] = env.ref("base.group_configuration") in user.groups_id
        except Exception as e:
            pass

        return self.request.render(template, context)


odootask_qweb_render = OdooTaskQwebRender(openerp.http.request)
