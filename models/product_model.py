class ProductModel:
    def __init__(self, title, price, description, add_to_cart_btn):
        self.title = title
        self.price = price
        self.description = description
        self.add_to_cart_btn = add_to_cart_btn

    def __repr__(self):
        return f"ProductModel(title={self.title}, price={self.price}, description={self.description})"

    def __eq__(self, other):
        return (
                self.title == other.title and
                self.price == other.price and
                self.description == other.description
        )