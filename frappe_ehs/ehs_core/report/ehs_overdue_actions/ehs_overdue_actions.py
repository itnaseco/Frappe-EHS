import frappe
from frappe import _
from frappe.utils import today


def execute(filters=None):
	columns = [
		{"fieldname": "name", "fieldtype": "Link", "label": _("Action"), "options": "EHS Action", "width": 150},
		{"fieldname": "action", "fieldtype": "Data", "label": _("Action"), "width": 280},
		{"fieldname": "owner", "fieldtype": "Link", "label": _("Owner"), "options": "User", "width": 180},
		{"fieldname": "due_date", "fieldtype": "Date", "label": _("Due Date"), "width": 110},
		{"fieldname": "status", "fieldtype": "Data", "label": _("Status"), "width": 120},
	]
	data = frappe.get_list(
		"EHS Action",
		filters={"due_date": ["<", today()], "status": ["!=", "Closed"]},
		fields=[column["fieldname"] for column in columns],
		order_by="due_date asc",
		page_length=500,
	)
	return columns, data
