from model.Product import Product
from view.ProductView import ProductView
from controller.ProductController import ProductController

model = Product.load_products()  # Carregue os produtos ao iniciar
view = ProductView()
controller = ProductController(model, view)

view.root.mainloop()
