# Library Management System
'''class library:
    def __init__(self):
        self.book={}

    def add_book(self,title):
        if title in self.book:
            print(f"book {title} is already in library")
        else:
            self.book[title]="availabe"
            print(f"book {title} is added into the library")

    def borrow_book(self,title):

        if title not in self.book:
            print(f"book {title}is not in library")
        elif self.book[title]=="borrowed":
            print(f"book {title} is already borrowed")
        else:
            self.book[title]="borrowed"
            print(f"book {title} b0rrowed from library ")

    def return_book(self,title):

        if title not in self.book:
            print(f"book {title} not exist in library")
        elif self.book[title]=="availabe":
            print(f"book {title} is already availabe")
        else:
            self.book[title]="availabe"
            print(f"book {title} returned successfully")

    def  display_books(self):
        if not self.book:
            print(f"books are not available in library")
        else:
            print("\ndisplay of all books")
            for title,status in self.book.items():
                print(title,":",status)


l=library()
l.add_book("python")
l.add_book("machine learning")
l.add_book("pycharm")
l.display_books()
l.return_book("xyz")
l.borrow_book("python")
l.return_book("python")'''

# 3. E-commerce Cart System
class shopping_cart :
    def __init__(self):
        self.cart={}
        self.discount=0
    def add_items(self,name,price,quantity=1):
        if name in self.cart:
            self.cart[name][quantity]+=quantity
        else:
            self.cart[name]={"price":price,"quantity":quantity}
            print(f"item {name} is successfully added")

    def remove_item(self,name,quantity):
        if name in self.cart:
            if self.cart[name]["quantity"]>quantity:
               self.cart[name]["quantity"] -=quantity 
               print(f"{quantity} item {name} is removed from the list") 
            else:
                del self.cart[name]
                print(f"{quantity} item {name} is removed from the list")
        else:
            print(f"item {name} is not found in the cart")    

    def view_cart(self):
        if not self.cart:
            print("your cart is empty")
            return

        print("shopping cart :")
        total=0
        for name,detail in self.cart.items():
            item_total=detail["price"]*detail["quantity"]
            total+=item_total
            print(f"item {name}  : price {detail["price"]} :quantity{detail["quantity"]}")
        if self.discount:
            discount_amount=total*(self.discount/100)
            total-=discount_amount
        print(f"the total price of cart is {total}")

    def apply_discount(self,discount_code):
        discount_codes={"IFS10":10,"IFS20":20,"IFS30":30}
        if discount_code in discount_codes:
            self.discount=discount_codes[discount_code]
            print(f"discount_code applied : {self.discount}% off")
        else:
            print("invalid discount code")

s= shopping_cart()
# s.add_items("bottle",150,3)
# s.add_items("shoes",1150,2)
# s.add_items("hand beg",100,1)
# s.remove_item("shoes",1)
# s.view_cart()         
s.view_cart()






























