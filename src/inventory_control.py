class InventoryControl:
    INGREDIENTS = {
        "hamburguer": ["pao", "carne", "queijo"],
        "pizza": ["massa", "queijo", "molho", "tomate"],
        "queijo-quente": ["pao", "queijo", "queijo"],
        "misto-quente": ["pao", "queijo", "presunto"],
        "bauru": ["pao", "queijo", "presunto", "tomate"],
        "coxinha": ["massa", "frango"],
    }
    MINIMUM_INVENTORY = {
        "pao": 50,
        "carne": 50,
        "queijo": 100,
        "molho": 50,
        "presunto": 50,
        "massa": 50,
        "frango": 50,
    }

    def __init__(self):
        self.dishes = {
            "hamburguer": ["pao", "carne", "queijo"],
            "pizza": ["massa", "queijo", "molho"],
            # 'queijo-quente': ['pao', 'queijo', 'queijo'],
            "misto-quente": ["pao", "queijo", "presunto"],
            # 'bauru': ['pao', 'queijo', 'presunto'],
            "coxinha": ["massa", "frango"],
        }
        self.minimum_inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }
        self.inventory = {
            "pao": 50,
            "carne": 50,
            "queijo": 100,
            "molho": 50,
            "presunto": 50,
            "massa": 50,
            "frango": 50,
        }

    def add_new_order(self, costumer, order, day):
        for ingredient in self.dishes[order]:
            if self.inventory[ingredient] > 0:
                self.inventory[ingredient] -= 1
            else:
                return False

    def get_quantities_to_buy(self):
        to_buy = self.minimum_inventory
        for ingredient in self.inventory.keys():
            to_buy[ingredient] = (
                to_buy[ingredient] - self.inventory[ingredient]
            )
        return to_buy

    def get_available_dishes(self):
        available_ingredients = set()
        dishes = set()
        for ingredient in self.inventory:
            if self.inventory[ingredient] > 0:
                available_ingredients.add(ingredient)
        for dish in self.dishes:
            if available_ingredients > set(self.dishes[dish]):
                dishes.add(dish)
        return dishes
