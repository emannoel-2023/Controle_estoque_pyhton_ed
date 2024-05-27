# ProductController.py
from model.Product import Product
import tkinter as tk

class ProductController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.add_button.config(command=self.add_product)
        self.view.update_button.config(command=self.update_product)
        self.view.delete_button.config(command=self.delete_product)
        self.view.exit_button.config(command=self.exit_system)  # Configure o comando do botão de sair
        self.view.product_list.bind('<<TreeviewSelect>>', self.select_product)
        self.selected_product_id = None

        self.view.update_product_list(self.model)  # Atualize a lista de produtos ao iniciar

    def add_product(self):
        name = self.view.entry_name.get()
        brand = self.view.entry_brand.get()
        price = self.view.entry_price.get()
        quantity = self.view.entry_quantity.get()
        description = self.view.entry_description.get()
        if not name or not brand or not price or not quantity or not description:
            self.view.show_error_message("Todos os campos devem ser preenchidos.")
            return
        id = 'I' + str(len(self.model) + 1).zfill(3)
        product = Product(id, name, brand, price, quantity, description)
        self.model.append(product)
        self.view.product_list.insert('', 'end', values=(product.id, name, brand, price, quantity, description))
        self.view.clear_entries()

    def update_product(self):
        selected = self.view.product_list.selection()
        if not selected:
            self.view.show_error_message("Nenhum produto selecionado.")
            return
        self.selected_product_id = self.view.product_list.item(selected[0])['values'][0]
        name = self.view.entry_name.get()
        brand = self.view.entry_brand.get()
        price = self.view.entry_price.get()
        quantity = self.view.entry_quantity.get()
        description = self.view.entry_description.get()
        if not name or not brand or not price or not quantity or not description:
            self.view.show_error_message("Todos os campos devem ser preenchidos.")
            return
        product = Product(self.selected_product_id, name, brand, price, quantity, description)
        self.model[self.model.index(next(p for p in self.model if p.id == self.selected_product_id))] = product
        self.view.product_list.delete(selected[0])
        self.view.product_list.insert('', self.model.index(product), values=(product.id, name, brand, price, quantity, description))
        self.view.clear_entries()

    def delete_product(self):
        selected = self.view.product_list.selection()
        if not selected:
            self.view.show_error_message("Nenhum produto selecionado.")
            return
        self.selected_product_id = self.view.product_list.item(selected[0])['values'][0]
        self.model.remove(next(p for p in self.model if p.id == self.selected_product_id))
        self.view.product_list.delete(selected[0])
        self.view.clear_entries()

    def select_product(self, event):
        selected = self.view.product_list.selection()
        if selected:
            selected_product_id = self.view.product_list.item(selected[0])['values'][0]
            # Adicione uma verificação para evitar atualizar os campos se o produto selecionado for o mesmo
            if selected_product_id != self.selected_product_id:
                self.selected_product_id = selected_product_id
                product = next((p for p in self.model if p.id == self.selected_product_id), None)
                if product is not None:
                    self.view.fill_entries(product)

    def exit_system(self):
        Product.save_products(self.model)  # Salve os produtos ao sair
        self.view.root.quit()