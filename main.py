from Product import Product
from ProductView import ProductView
from ProductController import ProductController

model = Product.load_products()  # Carregue os produtos ao iniciar
view = ProductView()
controller = ProductController(model, view)

view.root.mainloop()
