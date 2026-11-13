import json
from pathlib import Path

from frappe.tests import UnitTestCase


APP_ROOT = Path(__file__).resolve().parents[1]


class TestSchema(UnitTestCase):
	def test_all_json_files_parse(self):
		for path in APP_ROOT.rglob("*.json"):
			with self.subTest(path=path):
				json.loads(path.read_text())

	def test_role_fixtures_include_role_name(self):
		roles = json.loads((APP_ROOT / "fixtures" / "role.json").read_text())
		for role in roles:
			with self.subTest(role=role["name"]):
				self.assertEqual(role["role_name"], role["name"])

	def test_optional_apps_are_not_hard_links(self):
		optional_doctypes = {"Employee", "Supplier", "Item", "Asset", "Project"}
		for path in APP_ROOT.glob("ehs_*/doctype/*/*.json"):
			doc = json.loads(path.read_text())
			for field in doc.get("fields", []):
				if field.get("fieldtype") == "Link":
					self.assertNotIn(field.get("options"), optional_doctypes, path.name)

	def test_frequent_filters_are_indexed(self):
		required = {
			"EHS Incident": {"incident_date", "site", "status"},
			"EHS Action": {"due_date", "status"},
			"EHS Regulatory Permit": {"expiry_date", "status"},
			"EHS Work Permit": {"valid_until", "site", "status"},
		}
		for path in APP_ROOT.glob("ehs_*/doctype/*/*.json"):
			doc = json.loads(path.read_text())
			if doc.get("name") not in required:
				continue
			indexed = {field["fieldname"] for field in doc["fields"] if field.get("search_index")}
			self.assertTrue(required[doc["name"]].issubset(indexed), doc["name"])
