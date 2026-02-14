from django.test import TestCase
from pos.services.menu_service import MenuService
from pos.services.order_service import OrderService
from pos.models import Order, OrderItem


class OrderServiceTest(TestCase):
    def setUp(self):
        self.menu_service = MenuService()
        self.order_service = OrderService(self.menu_service)
    
    def test_single_item_order(self):
        """Test ordering a single item."""
        order = Order(items=[
            OrderItem(menu_item_id='cheeseburger', quantity=1)
        ])
        receipt = self.order_service.process_order(order)
        
        self.assertEqual(len(receipt.line_items), 1)
        self.assertEqual(receipt.line_items[0].name, 'Cheeseburger')
        self.assertEqual(receipt.line_items[0].quantity, 1)
        self.assertEqual(receipt.total, 15.00)
    
    def test_multiple_items_order(self):
        """Test ordering multiple different items."""
        order = Order(items=[
            OrderItem(menu_item_id='cheeseburger', quantity=2),
            OrderItem(menu_item_id='soft_drink_large', quantity=1)
        ])
        receipt = self.order_service.process_order(order)
        
        self.assertEqual(len(receipt.line_items), 2)
        self.assertEqual(receipt.total, 35.00)
    
    def test_duplicate_items_grouped(self):
        """Test that duplicate items are grouped together."""
        order = Order(items=[
            OrderItem(menu_item_id='cheeseburger', quantity=2),
            OrderItem(menu_item_id='cheeseburger', quantity=3)
        ])
        receipt = self.order_service.process_order(order)
        
        # Should be grouped into one line item
        self.assertEqual(len(receipt.line_items), 1)
        self.assertEqual(receipt.line_items[0].quantity, 5)
        self.assertEqual(receipt.line_items[0].subtotal, 75.00)
    
    def test_gst_calculation(self):
        """Test that GST is calculated correctly (extracted from inclusive price)."""
        order = Order(items=[
            OrderItem(menu_item_id='cheeseburger', quantity=2),
            OrderItem(menu_item_id='soft_drink_large', quantity=1)
        ])
        receipt = self.order_service.process_order(order)
        
        # Total is $35, GST should be $35 * (0.1/1.1) = $3.18 (rounded)
        self.assertEqual(receipt.total, 35.00)
        self.assertAlmostEqual(receipt.tax, 3.18, places=2)
        self.assertAlmostEqual(receipt.subtotal, 31.82, places=2)
    
    def test_empty_order(self):
        """Test handling of empty order."""
        order = Order(items=[])
        receipt = self.order_service.process_order(order)
        
        self.assertEqual(len(receipt.line_items), 0)
        self.assertEqual(receipt.total, 0.0)
        self.assertEqual(receipt.tax, 0.0)