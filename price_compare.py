class Compare:

    def __init__(self, current_price, top_price):
        self.product_current_price = current_price
        self.top_price = top_price

    def price_compare(self):
        return self.product_current_price < self.top_price

