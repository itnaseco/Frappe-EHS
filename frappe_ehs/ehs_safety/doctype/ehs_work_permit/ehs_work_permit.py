from frappe.model.document import Document

from frappe_ehs.validation import validate_date_order


class EHSWorkPermit(Document):
	def validate(self):
		validate_date_order(self.valid_from, self.valid_until, label="Permit validity")
