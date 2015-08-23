{
    'name': "Odoo Task",
    'version': '1.0',
    'depends': ['base', "mail"],
    'author': "Wangting",
    'category': 'Category',
    'description': """
    Description text 2
    """,
    # # data files always loaded at installation
    'data': [
        "data/group.xml",
        "workflow/odootask_workflow.xml",
        'templates/base.xml',
        'templates/index.xml',
        'templates/task.xml',
        "templates/about.xml",
        "templates/team.xml",
        "templates/user.xml",
        "views/task.xml"
    ],
    # # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo_data.xml',
    # ],
}
