import frappe
from frappe import _
from frappe.model.document import Document

from frappe_ehs.validation import validate_dynamic_link


class EHSAction(Document):
	def validate(self):
		validate_dynamic_link(self.source_type, self.source_name, label="Action source")
		if self.status == "Closed" and not self.completion_evidence:
			frappe.throw(_("Completion Evidence is required before an action can close"))
		if self.status == "Closed" and not self.verified_by:
			frappe.throw(_("Verified By is required before an action can close"))
		if self.status == "Closed" and self.verified_by == self.owner:
			frappe.throw(_("The action owner cannot verify the same action"))
