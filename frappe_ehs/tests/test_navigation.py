import json
from pathlib import Path

from frappe.tests import UnitTestCase


APP_ROOT = Path(__file__).resolve().parents[1]


class TestNavigation(UnitTestCase):
	def test_workspace_doctype_links_resolve_to_shipped_doctypes(self):
		doctypes = {path.stem for path in APP_ROOT.glob("ehs_*/doctype/*/*.json")}
		for workspace_path in APP_ROOT.glob("ehs_*/workspace/*/*.json"):
			workspace = json.loads(workspace_path.read_text())
			for item in workspace.get("sidebar_items", []):
				if item.get("link_type") == "DocType":
					self.assertIn(item.get("link_to"), doctypes, workspace_path.name)

	def test_dock_workspace_links_resolve(self):
		workspaces = {
			json.loads(path.read_text())["name"] for path in APP_ROOT.glob("ehs_*/workspace/*/*.json")
		}
		dock = json.loads((APP_ROOT / "dock/frappe_ehs/frappe_ehs.json").read_text())
		for item in dock["items"]:
			self.assertIn(item["link_to"], workspaces)

	def test_overview_references_shipped_cards(self):
		cards = {json.loads(path.read_text())["name"] for path in APP_ROOT.glob("ehs_*/number_card/*/*.json")}
		overview = json.loads((APP_ROOT / "ehs_core/workspace/ehs_overview/ehs_overview.json").read_text())
		for card in overview["number_cards"]:
			self.assertIn(card["number_card_name"], cards)
