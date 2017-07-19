# Copyright (c) 2013, Console ERP and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
	import erpnext.accounts.report.trial_balance.trial_balance
	columns, data = erpnext.accounts.report.trial_balance.trial_balance.execute(filters)

	data[-1]["closing_credit"] = 0
	data[-1]["opening_credit"] = 0
	data[-1]["closing_debit"] = 0
	data[-1]["opening_debit"] = 0
	for i in [x for x in data if x.get("indent",-1) == 0 and x != data[-1]]:
		print(i)
		data[-1]["closing_credit"] += i.get("closing_credit", 0)
		data[-1]["closing_debit"] += i.get("closing_debit", 0)
		data[-1]["opening_credit"] += i.get("opening_credit", 0)
		data[-1]["opening_debit"] += i.get("opening_debit", 0)
	
	return columns, data
