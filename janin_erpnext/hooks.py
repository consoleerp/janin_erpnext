# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "janin_erpnext"
app_title = "Janin Erpnext"
app_publisher = "Console ERP"
app_description = "ERPNext Customizations for Janin"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@consoleerp.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/janin_erpnext/css/janin_erpnext.css"
# app_include_js = "/assets/janin_erpnext/js/janin_erpnext.js"

# include js, css files in header of web template
# web_include_css = "/assets/janin_erpnext/css/janin_erpnext.css"
# web_include_js = "/assets/janin_erpnext/js/janin_erpnext.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "janin_erpnext.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "janin_erpnext.install.before_install"
# after_install = "janin_erpnext.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "janin_erpnext.notifications.get_notification_config"

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

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"janin_erpnext.tasks.all"
# 	],
# 	"daily": [
# 		"janin_erpnext.tasks.daily"
# 	],
# 	"hourly": [
# 		"janin_erpnext.tasks.hourly"
# 	],
# 	"weekly": [
# 		"janin_erpnext.tasks.weekly"
# 	]
# 	"monthly": [
# 		"janin_erpnext.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "janin_erpnext.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "janin_erpnext.event.get_events"
# }

