from market import app
from market.models import add_item
add_item("Iphone 15 pro", 1200000, "ABCDEF123412", "Iphone make you very simple")
add_item("Apple Laptop", 1200000, "Acdbef123412", "ILaptop make you very simple")
add_item("Mouses",120,"abcdefghijkl","A lighting mouse")
if __name__=='__main__':
    app.run(debug=True)