import frappe
from frappe.tests import UnitTestCase

from frappe_ehs.validation import validate_date_order, validate_dynamic_link, validate_positive


class TestValidation(UnitTestCase):
	def test_date_order_accepts_equal_dates(self):
		validate_date_order("2026-01-01", "2026-01-01", label="Validity")

	def test_date_order_rejects_reversed_dates(self):
		with self.assertRaises(frappe.ValidationError):
			validate_date_order("2026-01-02", "2026-01-01", label="Validity")

	def test_positive_value_rejects_zero(self):
		with self.assertRaises(frappe.ValidationError):
			validate_positive(0, label="Quantity")

	def test_dynamic_link_requires_both_values(self):
		with self.assertRaises(frappe.ValidationError):
			validate_dynamic_link("User", None, label="Recipient")
