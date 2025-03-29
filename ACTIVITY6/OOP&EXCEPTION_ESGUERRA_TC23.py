class Item:
    def __init__(self, item_id, name, description, price):
        self.item_id = item_id
        self.name = name
        self.description = description
        self.price = price

class ItemManager:
    def __init__(self):
        self.items = {}

    def create_item(self):
        try:
            item_id = int(input("Enter item ID (positive number): "))
            if item_id <= 0:
                print("\nID must be a positive number.")
                return
            name = input("Enter item name: ")
            description = input("Enter item description: ")
            price = float(input("Enter item price: $"))
            if price < 0:
                print("\nPrice must be a positive number.")
                return
            item = Item(item_id, name, description, price)
            self.items[item_id] = item
            print("\nItem added successfully.")
        except ValueError:
            print("\nInvalid input. Please enter valid data.")

    def read_item(self):
        try:
            item_id = int(input("\nEnter item ID to read: "))
            item = self.items.get(item_id)
            if item:
                print(f"ID: {item.item_id}, Name: {item.name}, Description: {item.description}, Price: ${item.price}")
            else:
                print("\nItem not found.")
        except ValueError:
            print("\nInvalid input. Item ID must be a number.")

    def update_item(self):
        try:
            item_id = int(input("\nEnter item ID to update: "))
            item = self.items.get(item_id)
            if item:
                name = input("Enter new item name (leave blank to keep current): ")
                description = input("Enter new item description (leave blank to keep current): ")
                price_input = input("Enter new item price (leave blank to keep current): ")
                if name:
                    item.name = name
                if description:
                    item.description = description
                if price_input:
                    price = float(price_input)
                    if price >= 0:
                        item.price = price
                    else:
                        print("\nPrice must be a positive number.")
                        return
                print("\nItem updated successfully.")
            else:
                print("\nItem not found.")
        except ValueError:
            print("\nInvalid input. Please enter valid data.")

    def delete_item(self):
        try:
            item_id = int(input("\nEnter item ID to delete: "))
            if item_id in self.items:
                del self.items[item_id]
                print("\nItem deleted successfully.")
            else:
                print("\nItem not found.")
        except ValueError:
            print("\nInvalid input. Item ID must be a number.")

    def show_all_items(self):
        if not self.items:
            print("\nNo items to display.")
        else:
            for item in self.items.values():
                print() 
                print(f"ID: {item.item_id}")
                print(f"Name: {item.name}")
                print(f"Description: {item.description}")
                print(f"Price: ${item.price}")

# Main program menu
def menu():
    manager = ItemManager()

    while True:
        print("\n========================")
        print("   * ITEM MANAGEMENT *   ")
        print("========================")
        print("[C] - Create Item")
        print("[R] - Read Item")
        print("[U] - Update Item")
        print("[D] - Delete Item")
        print("[S] - Show All Items")
        print("[Q] - Quit")
        print("------------------------")
        choice = input("Enter your choice: ").upper()

        if choice == 'Q':
            print("\nExiting program...")
            break

        elif choice == 'C':
            manager.create_item()

        elif choice == 'R':
            manager.read_item()

        elif choice == 'U':
            manager.update_item()

        elif choice == 'D':
            manager.delete_item()

        elif choice == 'S':
            manager.show_all_items()

        else:
            print("\nInvalid choice. Please try again.")

# Start the menu
if __name__ == "__main__":
    menu()
