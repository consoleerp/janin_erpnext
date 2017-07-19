from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
				{
					"label": _("Accounting Statements"),
					"items": [
						{
							"type": "report",
							"name": "Trial Balance Janin",
							"doctype": "GL Entry",
							"is_query_report": True,
						}
					]
				}
	]