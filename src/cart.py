class EmptyCartError(Exception):
    pass

class Cart:
    def __init__(self):
        self.items = []

    def add(self, name, price, qty=1):
        if price < 0:
            raise ValueError("price must be >= 0")
        self.items.append((name, price, qty))

    def total(self):
        if not self.items:
            raise EmptyCartError("cart is empty")
        return sum(p * q for name, p, q in self.items)