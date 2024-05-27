import os
import pickle

class Product:
    def __init__(self, id, name, brand, price, quantity, description):
        self.id = id
        self.name = name
        self.brand = brand
        self.price = price
        self.quantity = quantity
        self.description = description

    @staticmethod
    def save_products(products):
        file_path = os.path.join(os.path.dirname(__file__), 'products.pkl')
        with open(file_path, 'wb') as f:
            pickle.dump(products, f)

    @staticmethod
    def load_products():
        file_path = os.path.join(os.path.dirname(__file__), 'products.pkl')
        try:
            with open(file_path, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            return []
