class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.price} Kč"


class Pizza(Item):
    def __init__(self, name, price, ingredients):
        super().__init__(name, price)
        self.ingredients = ingredients

    def add_extra(self, ingredient, quantity, price_per_ingredient):
        self.ingredients[ingredient] = quantity
        self.price += quantity * price_per_ingredient

    def __str__(self):
        ingredient_list = ", ".join([f"{ingredient} ({quantity}g)" for ingredient, quantity in self.ingredients.items()])
        return f"{self.name} - Ingredients: {ingredient_list}, Price: {self.price} Kč"


class Drink(Item):
    def __init__(self, name, volume, price):
        super().__init__(name, price)
        self.volume = volume

    def __str__(self):
        return f"{self.name} - Volume: {self.volume} ml, Price: {self.price} Kč"


class Order:
    def __init__(self, customer_name, delivery_address, items):
        self.customer_name = customer_name
        self.delivery_address = delivery_address
        self.items = items
        self.status = "Nová"

    def mark_delivered(self):
        self.status = "Doručeno"

    def __str__(self):
        item_list = ", ".join([str(item) for item in self.items])
        return f"Order for: {self.customer_name}, Delivery Address: {self.delivery_address}, Items: {item_list}, Status: {self.status}"


class DeliveryPerson:
    def __init__(self, name, phone_number):
        self.name = name
        self.phone_number = phone_number
        self.available = True
        self.current_order = None

    def assign_order(self, order):
        if self.available:
            self.current_order = order
            order.status = "Na cestě"
            self.available = False

    def complete_delivery(self):
        if self.current_order:
            self.current_order.mark_delivered()
            self.current_order = None
            self.available = True

    def __str__(self):
        availability = "Available" if self.available else "Not Available"
        return f"Delivery Person: {self.name}, Phone: {self.phone_number}, Status: {availability}"


# Příklad použití

# Vytvoření instance pizzy
margarita = Pizza("Margarita", 200, {"sýr": 100, "rajčata": 150})
margarita.add_extra("olivy", 50, 10)

# Vytvoření instance nápoje
cola = Drink("Cola", 1500, 50)

# Vytvoření objednávky
order = Order("Jan Novák", "Pražská 123", [margarita, cola])

# Vytvoření doručovatele
delivery_person = DeliveryPerson("Petr Novotný", "777 888 999")

# Přiřazení objednávky doručovateli
delivery_person.assign_order(order)

# Dokončení doručení
delivery_person.complete_delivery()

# Výpis stavu objednávky po doručení
print(order)