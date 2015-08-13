__author__ = 'wt'
import openerp.http
from openerp.http import request
from base import odootask_qweb_render
import math


class TaskController(openerp.http.Controller):
    @openerp.http.route("/tasks", type='http', auth="public", methods=["GET"])
    def index(self, **kwargs):
        para_keyword = kwargs.get("k", "")
        para_category_id = kwargs.get("c", "")
        order = kwargs.get("o", "create_date")
        page = int(kwargs.get("p", "0"))
        qty_per_page = int(kwargs.get("n", "10"))

        domain = list()
        if para_keyword:
            domain.append(("name", "ilike", para_keyword))
        if para_category_id:
            domain.append(("category_id", "=", int(para_category_id)))

        env = request.env

        total_page_count = int(math.ceil(env['odootask.task'].sudo().search_count(domain) / float(qty_per_page)))
        tasks = env['odootask.task'].sudo().search(domain, order="%s desc" % order, offset=page * qty_per_page,
                                                   limit=qty_per_page)
        categories = env["odootask.task_category"].sudo().search([])

        count_for_category = [
            ((cat.name, cat.id),
             env['odootask.task'].sudo().search_count([("name", "ilike", para_keyword), ("category_id", "=", cat.id)]))
            for cat in categories]

        if para_keyword:
            count_for_category = filter(lambda cfc: cfc[1] > 0, count_for_category)

        count_for_category = dict(count_for_category)

        context = dict()
        context["tasks"] = tasks
        context["count_for_category"] = count_for_category
        if para_category_id:
            context["category_id"] = int(para_category_id)
        else:
            context["category_id"] = -1
        context["keyword"] = para_keyword

        context["main_nav_task_active"] = True
        context["login_redirect"] = "/tasks"

        return odootask_qweb_render.render("odootask.tasks", context=context)

    @openerp.http.route("/task/<int:task_id>", type='http', auth="public", methods=["GET"])
    def task(self, task_id=None, **kwargs):
        try:
            if not task_id:
                # TODO return 404
                pass
            env = request.env
            task = env['odootask.task'].sudo().search([("id", "=", task_id)])
            context = dict()
            context["task"] = task
            context["login_redirect"] = "/task/%d" % task_id
            context["ret_url"] = kwargs.get("ret_url")
            context["user_id"] = env.user.id
            return odootask_qweb_render.render("odootask.task", context=context)
        except Exception as e:
            pass

    @openerp.http.route("/task", type='http', auth="user", methods=["GET", "POST"])
    def new_task(self, **kwargs):
        if request.httprequest.method == 'GET':
            try:
                task_categories = request.env["odootask.task_category"].search([]);
                context = dict()
                context["task_categories"] = task_categories
                return odootask_qweb_render.render("odootask.task_new", context=context)
            except Exception as ex:
                pass
                # TODO Error handler
        elif request.httprequest.method == 'POST':
            name = kwargs.get("name", "")
            description = kwargs.get("description", "")
            category_id = kwargs.get("category_id", "")
            values = dict()
            values["name"] = name
            values["description"] = description
            if category_id:
                values["category_id"] = int(category_id)
            request.env["odootask.task"].create(values)
            return "create ok"
        else:
            return "only GET POST is available!"

    @openerp.http.route("/task/apply/<int:task_id>", type='http', auth="user", methods=["GET", "POST"])
    def apply_task(self, task_id=None):
        try:
            if not task_id:
                # TODO return 404
                pass
            env = request.env
            task = env['odootask.task'].sudo().search([("id", "=", task_id)])
            task.apply(env.user.id)
            return "apply ok"
        except Exception as e:
            pass

    @openerp.http.route("/task/<int:task_id>/comment", type='http', auth="user", methods=["POST"])  # "GET",
    def comment(self, task_id=None, **kwargs):
        if request.httprequest.method == 'POST':
            try:
                if not task_id:
                    # TODO return 404
                    pass
                content = kwargs.get("content", "")
                env = request.env
                task = env['odootask.task'].sudo().search([("id", "=", task_id)])
                if task:
                    env["odootask.task_comment"].create({"task_id": task.id, "content": content})
                    return "post comment ok"
            except Exception as e:
                pass
