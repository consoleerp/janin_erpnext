import frappe

def execute():
	frappe.db.sql("""UPDATE `tabAccount` SET account_name_arabic = account_name""")