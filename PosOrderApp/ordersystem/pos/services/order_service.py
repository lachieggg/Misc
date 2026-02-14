from collections import defaultdict
from typing import List
from pos.models import Order, Receipt, LineItem
from pos.services.menu_service import MenuService


class OrderService:
    def __init__(self, menu_service: MenuService):
        self.menu_service = menu_service

    def process_order(self, order: Order) -> Receipt:
        grouped_items = self._group_order_items(order)
        line_items, total = self._construct_line_items(grouped_items)
        tax, subtotal = self._calculate_tax_and_subtotal(total)

        return Receipt(line_items=line_items, subtotal=subtotal, tax=tax, total=total)

    def _group_order_items(self, order: Order) -> dict[str, int]:
        """Group order items by menu_item_id and sum quantities.

        Consolidates duplicate items to simplify the receipt display.
        E.g., two separate "cheeseburger x1" entries become "cheeseburger x2".
        """
        grouped = defaultdict(int)
        for order_item in order.items:
            grouped[order_item.menu_item_id] += order_item.quantity
        return grouped

    def _construct_line_items(
        self, grouped_items: dict[str, int]
    ) -> tuple[List[LineItem], float]:
        """Create line items from grouped order items and calculate total."""
        line_items = []
        total = 0.0

        for menu_item_id, quantity in grouped_items.items():
            menu_item = self.menu_service.get_item(menu_item_id)
            item_subtotal = menu_item.price * quantity

            line_items.append(
                LineItem(
                    name=menu_item.name,
                    quantity=quantity,
                    unit_price=menu_item.price,
                    subtotal=item_subtotal,
                )
            )
            total += item_subtotal

        return line_items, total

    def _calculate_tax_and_subtotal(self, total: float) -> tuple[float, float]:
        """Extract GST component from total (prices include GST).

        Menu prices are GST-inclusive, so we extract the tax component rather than adding it.
        Formula: tax = total × (rate / (1 + rate))
        E.g., for $35 total with 10% GST: tax = $35 × (0.1/1.1) = $3.18
        """
        tax_rate = self.menu_service.get_tax_rate()
        tax = total * (tax_rate / (1 + tax_rate))
        subtotal = total - tax
        return tax, subtotal
