from frappe.model.document import Document

from frappe_ehs.validation import validate_date_order


class EHSAudit(Document):
	def validate(self):
		validate_date_order(self.start_date, self.end_date, label="Audit period")
