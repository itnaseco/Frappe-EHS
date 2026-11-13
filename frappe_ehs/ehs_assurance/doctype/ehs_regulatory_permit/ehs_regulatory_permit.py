from frappe.model.document import Document

from frappe_ehs.validation import validate_date_order


class EHSRegulatoryPermit(Document):
	def validate(self):
		validate_date_order(self.issue_date, self.expiry_date, label="Regulatory permit")
