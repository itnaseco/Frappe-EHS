from datetime import date, datetime

import frappe
from frappe import _
from frappe.utils import flt, getdate


def validate_date_order(start: date | datetime | str | None, end: date | datetime | str | None, *, label: str) -> None:
	if start and end and getdate(end) < getdate(start):
		frappe.throw(_("{0}: end date cannot be before start date").format(label))


def validate_positive(value: float | int | str | None, *, label: str) -> None:
	if flt(value) <= 0:
		frappe.throw(_("{0} must be greater than zero").format(label))


def validate_dynamic_link(link_type: str | None, link_name: str | None, *, label: str) -> None:
	if bool(link_type) != bool(link_name):
		frappe.throw(_("{0} requires both a document type and a document name").format(label))
