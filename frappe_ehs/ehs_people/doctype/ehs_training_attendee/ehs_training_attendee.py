from frappe.model.document import Document

from frappe_ehs.validation import validate_dynamic_link


class EHSTrainingAttendee(Document):
	def validate(self):
		validate_dynamic_link(self.attendee_type, self.attendee, label="Attendee")
