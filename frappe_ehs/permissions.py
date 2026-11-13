import frappe


EHS_ROLES = {"EHS User", "EHS Officer", "EHS Manager", "EHS Administrator", "System Manager"}


def has_app_permission() -> bool:
	return bool(EHS_ROLES.intersection(frappe.get_roles()))
