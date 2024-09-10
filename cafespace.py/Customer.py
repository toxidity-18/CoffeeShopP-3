class Customer:
    def __init__(self, name):
        if not isinstance(name, str) or not (1 <= len(name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = name
        self._orders = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if not isinstance(new_name, str) or not (1 <= len(new_name) <= 15):
            raise ValueError("Customer name must be a string between 1 and 15 characters.")
        self._name = new_name

    def orders(self):
        return self._orders

    def coffees(self):
        return list(set(order.coffee for order in self._orders))

    def create_order(self, coffee, price):
        order = Order(self, coffee, price)
        self._orders.append(order)
        coffee.add_order(order)
        return order

    @classmethod
    def most_aficionado(cls, coffee):
        if not coffee.orders():
            return None
        customer_spending = {}
        for order in coffee.orders():
            customer_spending[order.customer] = customer_spending.get(order.customer, 0) + order.price
        return max(customer_spending, key=customer_spending.get)

