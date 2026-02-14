import yaml
from pathlib import Path
from typing import Dict
from django.conf import settings
from pos.models import MenuItem


class MenuService:
    def __init__(self, config_path: str = None):
        if not config_path:
            # Use Django's BASE_DIR to ensure correct path regardless of where command is run
            config_path = Path(settings.BASE_DIR) / "pos" / "config" / "menu.yaml"
        self.config_path = Path(config_path)
        self._menu: Dict[str, MenuItem] = {}
        self._menu_by_id: Dict[int, MenuItem] = {}
        self._tax_rate: float = 0.0
        self._load_menu()

    def _load_menu(self):
        data = self._read_config_file()
        self._parse_menu_data(data)

    def _read_config_file(self) -> dict:
        """Load YAML configuration from file."""
        with open(self.config_path, "r") as f:
            return yaml.safe_load(f)

    def _parse_menu_data(self, data: dict):
        """Parse menu data and populate internal structures."""
        self._tax_rate = data.get("tax_rate", 0.10)
        self._build_menu_items(data["items"])

    def _build_menu_items(self, items_data: dict):
        """Construct MenuItem objects and populate lookup dictionaries."""
        for item_key, item_data in items_data.items():
            menu_item = MenuItem(
                id=item_key, name=item_data["name"], price=item_data["price"]
            )
            self._menu[item_key] = menu_item
            self._menu_by_id[item_data["id"]] = menu_item

    def get_item(self, item_id: str) -> MenuItem:
        return self._menu[item_id]

    def get_item_by_number(self, num: int) -> MenuItem:
        return self._menu_by_id[num]

    def get_all_items(self) -> Dict[str, MenuItem]:
        return self._menu

    def get_tax_rate(self) -> float:
        return self._tax_rate
