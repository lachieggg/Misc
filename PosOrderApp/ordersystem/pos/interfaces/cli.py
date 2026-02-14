from pos.models import Order, OrderItem
from pos.services.menu_service import MenuService
from pos.services.order_service import OrderService


class CLI:
    # --- Command Constants ---
    CMD_DONE = "done"
    CMD_HELP = "help"

    # --- Message Constants ---
    PROMPT = "> "
    HELP_INTRO = (
        "Enter items (number quantity), type 'help' for instructions, or 'done' to finish:"
    )
    INVALID_INPUT_MSG = (
        "Invalid input. Use format: number quantity (e.g., '1 2'), or type 'help'"
    )

    def __init__(self):
        self.menu_service = MenuService()
        self.order_service = OrderService(self.menu_service)

    def run(self):
        print("=== Restaurant Order System ===\n")
        self.display_menu()

        order = self.take_order()
        receipt = self.order_service.process_order(order)

        self.display_receipt(receipt)

    def display_menu(self):
        print("Menu:")
        # Get items with their numeric IDs and sort by numeric ID
        items_with_ids = []
        for num_id, menu_item in self.menu_service._menu_by_id.items():
            items_with_ids.append((num_id, menu_item))

        items_with_ids.sort(key=lambda x: x[0])

        for num_id, item in items_with_ids:
            print(f"  {num_id}. {item.name} - ${item.price:.2f}")
        print()

    def _print_help(self):
        print("\nHow to order:")
        print("  - Enter: [menu number] [quantity]")
        print("  - Example: '1 2' orders 2 Cheeseburgers")
        print(f"  - Type '{self.CMD_DONE}' when finished")
        print(f"  - You can enter multiple items before typing '{self.CMD_DONE}'\n")

    def take_order(self) -> Order:
        items = []
        print(self.HELP_INTRO)

        while True:
            user_input = input(self.PROMPT).strip()
            if self._handle_order_input(user_input, items):
                break  # User indicated they are done

        return Order(items=items)

    def _handle_order_input(self, user_input: str, items: list[OrderItem]) -> bool:
        """Handle one line of user input. Return True if the loop should end."""
        lower = user_input.lower()

        if lower == self.CMD_DONE:
            return True

        if lower == self.CMD_HELP:
            self._print_help()
            return False

        try:
            item_num, quantity = user_input.split()
            menu_item = self.menu_service.get_item_by_number(int(item_num))
            items.append(
                OrderItem(menu_item_id=menu_item.id, quantity=int(quantity))
            )
        except (ValueError, KeyError):
            print(self.INVALID_INPUT_MSG)

        return False

    def display_receipt(self, receipt):
        print("\n" + "=" * 40)
        for line in receipt.line_items:
            print(f"{line.name} x {line.quantity} ${line.subtotal:.2f}")

        print(f"\nTotal ${receipt.total:.2f}")
        print(f"Including GST (${receipt.tax:.2f})")
        print("=" * 40)