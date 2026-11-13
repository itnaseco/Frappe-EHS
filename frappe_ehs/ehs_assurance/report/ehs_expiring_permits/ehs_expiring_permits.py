import frappe
from frappe import _
from frappe.utils import add_days, today


def execute(filters=None):
	days = 60
	columns = [
		{"fieldname": "name", "fieldtype": "Link", "label": _("Permit"), "options": "EHS Regulatory Permit", "width": 150},
		{"fieldname": "permit_title", "fieldtype": "Data", "label": _("Title"), "width": 220},
		{"fieldname": "authority", "fieldtype": "Data", "label": _("Authority"), "width": 160},
		{"fieldname": "site", "fieldtype": "Link", "label": _("Site"), "options": "EHS Site", "width": 130},
		{"fieldname": "expiry_date", "fieldtype": "Date", "label": _("Expiry Date"), "width": 110},
		{"fieldname": "status", "fieldtype": "Data", "label": _("Status"), "width": 120},
	]
	data = frappe.get_list(
		"EHS Regulatory Permit",
		filters={"expiry_date": ["between", [today(), add_days(today(), days)]], "status": ["!=", "Closed"]},
		fields=[column["fieldname"] for column in columns],
		order_by="expiry_date asc",
		page_length=500,
	)
	return columns, data
