from . import __version__ as app_version

app_name = "soul_hr"
app_title = "Soul Hr"
app_publisher = "SOUL"
app_description = "SOUL HR"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "soul@soulunileaders.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/soul_hr/css/soul_hr.css"
# app_include_js = "/assets/soul_hr/js/soul_hr.js"

# include js, css files in header of web template
# web_include_css = "/assets/soul_hr/css/soul_hr.css"
# web_include_js = "/assets/soul_hr/js/soul_hr.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "soul_hr/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "soul_hr.install.before_install"
# after_install = "soul_hr.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "soul_hr.uninstall.before_uninstall"
# after_uninstall = "soul_hr.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "soul_hr.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	"Interview":{
		"before_save":"soul_hr.soul_hr.Doctype.interview.before_save"
	},
	"Job Offer":{
		"before_save":"soul_hr.soul_hr.Doctype.job_offer.before_save"
	},
	"Leave Application":{
        "on_update":"soul_hr.soul_hr.validations.leave_application.on_update",
        "on_submit":"soul_hr.soul_hr.validations.leave_application.on_submit",
		"validate":"soul_hr.soul_hr.validations.leave_application.validate",
		"on_cancel":"soul_hr.soul_hr.validations.leave_application.on_cancel"
    }

}
# /opt/bench/frappe-bench/apps/soul_hr/soul_hr/soul_hr/notification/custom_notification.py
# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"soul_hr.tasks.all"
# 	],
# 	"daily": [
# 		"soul_hr.tasks.daily"
# 	],
# 	"hourly": [
# 		"soul_hr.tasks.hourly"
# 	],
# 	"weekly": [
# 		"soul_hr.tasks.weekly"
# 	]
# 	"monthly": [
# 		"soul_hr.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "soul_hr.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "soul_hr.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "soul_hr.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]


# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"soul_hr.auth.validate"
# ]

after_migrate = [
        'soul_hr.patches.migrate_patch.add_roles',
        'soul_hr.patches.migrate_patch.set_custom_role_permission',
]

# fixtures = [
# 	{"dt": "Custom DocPerm", "filters": [
# 		[
# 			"parent", "not in", [
# 				"DocType"
# 			]
# 		]
# 	]},
#     {"dt": "Role"},
#     {"dt": "Role Profile"},
#     {"dt": "Module Profile"}
# ]
