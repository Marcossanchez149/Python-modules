#!/usr/bin/env python3

class NotEnoughItems(Exception):
    def __init__(self, message="There is not enough items"):
        super().__init__(message)


class Item():
    def __init__(self, name, type, rarity, quantity, value):
        self.name = name
        self.info = dict(name=name, type=type, rarity=rarity,
                         quantity=quantity, value=value)

    def get_total_value(self):
        return (self.info.get('quantity') * self.info.get('value'))

    def get_info(self):
        total = self.info.get('quantity') * self.info.get('value')
        return (f"{self.info.get('name')} ({self.info.get('type')}, "
                f"{self.info.get('rarity')}): {self.info.get('quantity')}"
                f"x @ {self.info.get('value')} gold each = {total} gold")


class Player():
    def __init__(self, name):
        self.name = name
        self.inventory = {}

    def get_info(self):
        print(f"=== {self.name}'s Inventory ===")
        for x in self.inventory.values():
            print(x.get_info())

    def add_item(self, item: Item):
        self.inventory[item.name] = item

    def get_inventory_stats(self):
        total_value = 0
        cont = 0
        categories = []
        for x in self.inventory.values():
            total_value += x.get_total_value()
            cont += x.info.get("quantity")
            categories += [x.info.get("type")]
        print(f"Inventory value: {total_value} gold")
        print(f"Item count: {cont} items")
        print(f"Categories: {categories}")

    def transaction(self, item_name, change):
        item_object = self.inventory[item_name]
        current_quantity = item_object.info['quantity']
        if (current_quantity + change < 0):
            raise (NotEnoughItems)
        else:
            item_object.info['quantity'] += change

    def get_potions(self, item_name):
        item_object = self.inventory[item_name]
        current_quantity = item_object.info['quantity']
        print(f"{self.name} potions: {current_quantity}")

    def get_value(self):
        total_value = 0
        for x in self.inventory.values():
            total_value += x.get_total_value()
        return (total_value)

    def get_num_items(self):
        cont = 0
        for x in self.inventory.values():
            cont += x.info.get("quantity")
        return cont

    def get_rarest_items(self):
        rarest_items = []
        for x in self.inventory.values():
            if (x.info.get("rarity") == "rare"):
                rarest_items += [x]
        return rarest_items


if __name__ == "__main__":
    print("=== Player Inventory System ===")
    item1 = Item("sword", "weapon", "rare", 1, 500)
    item2 = Item("potion", "consumable", "common", 5, 50)
    item3 = Item("shield", "armor", "uncommon", 1, 200)
    item4 = Item("potion", "consumable", "common", 0, 50)
    item5 = Item("magic_ring", "weapon", "rare", 1, 200)
    player1 = Player("Alice")
    player1.add_item(item1)
    player1.add_item(item2)
    player1.add_item(item3)
    player1.get_info()
    player1.get_inventory_stats()
    print("=== Transaction: Alice gives Bob 2 potions ===")
    player2 = Player("Bob")
    player2.add_item(item4)
    player2.add_item(item5)
    try:
        player1.transaction("potion", -2)
        player2.transaction("potion", 2)
        print("Transaction successful!")
    except NotEnoughItems as e:
        print(f"Error: {e}")
    print("=== Updated Inventories ===")
    player1.get_potions("potion")
    player2.get_potions("potion")
    print("=== Inventory Analytics ===")
    if (player1.get_value() > player2.get_value()):
        print(f"Most valuable player: {player1.name} "
              f"({player1.get_value()} gold)")
    else:
        print(f"Most valuable player: {player2.name} "
              f"({player2.get_value()} gold)")
    if (player1.get_num_items() > player2.get_num_items()):
        print(f"Most items: {player1.name} "
              f"({player1.get_num_items()} items)")
    else:
        print(f"Most items: {player2.name} "
              f"({player2.get_num_items()} items)")
    rarest_items = player1.get_rarest_items()
    rarest_items += player2.get_rarest_items()
    item_names = [item.info.get("name") for item in rarest_items]
    print(f"Rarest items: {item_names}")
