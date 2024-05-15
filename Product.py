import pickle  # Importe o módulo pickle

class Product:
    def __init__(self, id, name, brand, price, quantity, description):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.description = description

    def save_products(products):
        with open('products.pkl', 'wb') as f:
            pickle.dump(products, f)

    def load_products():
        try:
            with open('products.pkl', 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
