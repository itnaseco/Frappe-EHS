from frappe.model.document import Document

from frappe_ehs.validation import validate_dynamic_link


class EHSFinding(Document):
	def validate(self):
		validate_dynamic_link(self.source_type, self.source_name, label="Finding source")
