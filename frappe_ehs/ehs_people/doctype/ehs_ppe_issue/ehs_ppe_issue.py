from frappe.model.document import Document

from frappe_ehs.validation import validate_date_order, validate_dynamic_link, validate_positive


class EHSPPEIssue(Document):
	def validate(self):
		validate_dynamic_link(self.recipient_type, self.recipient, label="Recipient")
		validate_positive(self.quantity, label="Quantity")
		validate_date_order(self.issue_date, self.replacement_date, label="PPE replacement")
