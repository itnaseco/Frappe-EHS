import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{"fieldname": "name", "fieldtype": "Link", "label": _("Training Event"), "options": "EHS Training Event", "width": 150},
		{"fieldname": "course", "fieldtype": "Link", "label": _("Course"), "options": "EHS Training Course", "width": 220},
		{"fieldname": "training_date", "fieldtype": "Date", "label": _("Date"), "width": 110},
		{"fieldname": "site", "fieldtype": "Link", "label": _("Site"), "options": "EHS Site", "width": 130},
		{"fieldname": "trainer", "fieldtype": "Data", "label": _("Trainer"), "width": 160},
		{"fieldname": "status", "fieldtype": "Data", "label": _("Status"), "width": 110},
	]
	data = frappe.get_list(
		"EHS Training Event",
		fields=[column["fieldname"] for column in columns],
		order_by="training_date desc",
		page_length=500,
	)
	return columns, data
