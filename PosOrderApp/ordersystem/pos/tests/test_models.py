from django.test import TestCase
from pos.models import MenuItem, OrderItem, Order, LineItem, Receipt


class ModelsTest(TestCase):
    def test_menu_item_creation(self):
        """Test MenuItem model creation."""
        item = MenuItem(id='test', name='Test Item', price=10.00)
        self.assertEqual(item.id, 'test')
        self.assertEqual(item.name, 'Test Item')
        self.assertEqual(item.price, 10.00)
    
    def test_order_item_creation(self):
        """Test OrderItem model creation."""
        order_item = OrderItem(menu_item_id='cheeseburger', quantity=2)
        self.assertEqual(order_item.menu_item_id, 'cheeseburger')
        self.assertEqual(order_item.quantity, 2)
    
    def test_order_creation(self):
        """Test Order model with items."""
        order = Order(items=[
            OrderItem(menu_item_id='cheeseburger', quantity=1),
            OrderItem(menu_item_id='soft_drink_small', quantity=2)
        ])
        self.assertEqual(len(order.items), 2)
    
    def test_receipt_creation(self):
        """Test Receipt model creation."""
        line_items = [
            LineItem(name='Test', quantity=1, unit_price=10.0, subtotal=10.0)
        ]
        receipt = Receipt(
            line_items=line_items,
            subtotal=9.09,
            tax=0.91,
            total=10.00
        )
        self.assertEqual(len(receipt.line_items), 1)
        self.assertAlmostEqual(receipt.total, 10.00)