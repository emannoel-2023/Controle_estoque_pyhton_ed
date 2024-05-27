# ProductView.py
import tkinter as tk
from tkinter import messagebox, ttk

class ProductView:
    def __init__(self):
        self.root = tk.Tk()

        tk.Label(self.root, text="Itens no estoque").pack()
        self.product_list = ttk.Treeview(self.root, columns=('ID', 'Nome', 'Marca', 'Preço', 'Quantidade', 'Descrição'), show='headings')
        self.product_list.column('ID', width=0, stretch=tk.NO)  # Torne a coluna ID invisível
        self.product_list.pack()
        for col in ('ID', 'Nome', 'Marca', 'Preço', 'Quantidade', 'Descrição'):
            self.product_list.heading(col, text=col)

        tk.Label(self.root, text="Nome do produto").pack()
        self.entry_name = tk.Entry(self.root)
        self.entry_name.pack()

        tk.Label(self.root, text="Marca do produto").pack()
        self.entry_brand = tk.Entry(self.root)
        self.entry_brand.pack()

        tk.Label(self.root, text="Preço do produto").pack()
        self.entry_price = tk.Entry(self.root)
        self.entry_price.pack()

        tk.Label(self.root, text="Quantidade do produto").pack()
        self.entry_quantity = tk.Entry(self.root)
        self.entry_quantity.pack()

        tk.Label(self.root, text="Descrição do produto").pack()
        self.entry_description = tk.Entry(self.root)
        self.entry_description.pack()

        self.add_button = tk.Button(self.root, text="Adicionar produto")
        self.add_button.pack()
        self.update_button = tk.Button(self.root, text="Atualizar produto selecionado")
        self.update_button.pack()
        self.delete_button = tk.Button(self.root, text="Remover produto selecionado")
        self.delete_button.pack()
        self.exit_button = tk.Button(self.root, text="Sair do sistema")  # Adicione o botão de sair
        self.exit_button.pack()

    def show_error_message(self, message):
        messagebox.showerror("Erro", message)

    def clear_entries(self):
        self.entry_name.delete(0, tk.END)
        self.entry_brand.delete(0, tk.END)
        self.entry_price.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)
        self.entry_description.delete(0, tk.END)

    def fill_entries(self, product):
        self.clear_entries()  # Limpe os campos de entrada antes de preenchê-los
        self.entry_name.insert(0, product.name)
        self.entry_brand.insert(0, product.brand)
        self.entry_price.insert(0, product.price)
        self.entry_quantity.insert(0, product.quantity)
        self.entry_description.insert(0, product.description)

    def update_product_list(self, products):  # Adicione este método
        for product in products:
            self.product_list.insert('', 'end', values=(product.id, product.name, product.brand, product.price, product.quantity, product.description))