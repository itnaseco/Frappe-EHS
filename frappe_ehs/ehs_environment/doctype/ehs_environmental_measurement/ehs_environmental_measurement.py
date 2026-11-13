from frappe.model.document import Document
from frappe.utils import flt


class EHSEnvironmentalMeasurement(Document):
	def validate(self):
		self.status = "Exceeded" if self.limit_value is not None and flt(self.value) > flt(self.limit_value) else "Within Limit"
