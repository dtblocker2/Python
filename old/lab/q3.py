class cart():
    def __init__(self):
        self.cart = {}
    
    def add_item(self,item,price,quantity):
        if item in self.cart:
            self.cart[item]["quantity"] += quantity
            self.cart[item]["price"] = price
        else:
            self.cart[item] = {"quantity": quantity, "price": price}

    def update_price(self,item,price):
        self.cart[item]["price"] = price
    
    def buy_item(self,item,quantity):
        if item in self.cart:
            if quantity<=self.cart[item]["quantity"]:
                self.cart[item]["quantity"] -= quantity
            else:
                print(f"Not enough {item}(s) in cart")
        else:
            print(f"Error {item} not in cart")
    
    def view_cart(self):
        for i in self.cart:
            print(f"{i}\nQuantity:{self.cart[i]["quantity"]}\nPrice:{self.cart[i]["price"]}\n")

A = cart()
A.add_item("Apple",69,77)
A.view_cart()