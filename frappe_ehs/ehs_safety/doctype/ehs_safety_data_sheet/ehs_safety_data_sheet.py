from frappe.model.document import Document

from frappe_ehs.validation import validate_date_order


class EHSSafetyDataSheet(Document):
	def validate(self):
		validate_date_order(self.version_date, self.review_date, label="SDS review")
