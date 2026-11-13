import frappe
from frappe import _


def execute(filters=None):
	columns = [
		{"fieldname": "name", "fieldtype": "Link", "label": _("Incident"), "options": "EHS Incident", "width": 150},
		{"fieldname": "incident_date", "fieldtype": "Datetime", "label": _("Date"), "width": 150},
		{"fieldname": "site", "fieldtype": "Link", "label": _("Site"), "options": "EHS Site", "width": 130},
		{"fieldname": "incident_type", "fieldtype": "Data", "label": _("Type"), "width": 130},
		{"fieldname": "severity", "fieldtype": "Data", "label": _("Severity"), "width": 100},
		{"fieldname": "status", "fieldtype": "Data", "label": _("Status"), "width": 120},
	]
	data = frappe.get_list(
		"EHS Incident",
		filters={"status": ["!=", "Closed"]},
		fields=[column["fieldname"] for column in columns],
		order_by="incident_date desc",
		page_length=500,
	)
	return columns, data
