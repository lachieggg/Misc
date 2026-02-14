from django.test import TestCase
from pathlib import Path
from pos.services.menu_service import MenuService
from pos.models import MenuItem


class MenuServiceTest(TestCase):
    def setUp(self):
        # Use the actual menu.yaml for testing
        self.menu_service = MenuService()
    
    def test_loads_menu_items(self):
        """Test that menu items are loaded correctly."""
        items = self.menu_service.get_all_items()
        self.assertGreater(len(items), 0)
    
    def test_get_item_by_string_id(self):
        """Test retrieving item by string ID."""
        item = self.menu_service.get_item('cheeseburger')
        self.assertEqual(item.name, 'Cheeseburger')
        self.assertEqual(item.price, 15.00)
    
    def test_get_item_by_number(self):
        """Test retrieving item by numeric ID."""
        item = self.menu_service.get_item_by_number(1)
        self.assertEqual(item.name, 'Cheeseburger')
        self.assertEqual(item.price, 15.00)
    
    def test_tax_rate_loaded(self):
        """Test that tax rate is loaded correctly."""
        tax_rate = self.menu_service.get_tax_rate()
        self.assertEqual(tax_rate, 0.10)
    
    def test_all_menu_items_present(self):
        """Test that all expected menu items are loaded."""
        items = self.menu_service.get_all_items()
        expected_items = ['cheeseburger', 'chicken_burger', 'soft_drink_small', 'soft_drink_large']
        for expected in expected_items:
            self.assertIn(expected, items)