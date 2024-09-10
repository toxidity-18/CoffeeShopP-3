class Order:
    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise ValueError("Order must have a Customer instance.")
        if not isinstance(coffee, Coffee):
            raise ValueError("Order must have a Coffee instance.")
        if not isinstance(price, (float, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("Price must be a float between 1.0 and 10.0.")
        
        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

    @property
    def price(self):
        return self._price

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee