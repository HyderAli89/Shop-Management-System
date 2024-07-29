class Owner:
    product_in_shop = {}
    expenses = {}

    def add_product(self):
        while True:
            z = int(input("Enter 1 to add Product and 2 to stop adding product: "))
            if z == 1:
                product = input("Enter Product Name: ")
                price = int(input("Enter Price: "))
                self.product_in_shop.update({price: product})
            else:
                break

    def remove_product(self):
        while True:
            z = int(input("Enter 1 to remove Product and 2 to stop removing product: "))
            if z == 1:
                product = input("Enter Product to be removed: ")
                product_to_remove = []

                for key, value in self.product_in_shop.items():
                    if value == product:
                        product_to_remove.append(key)

                if product_to_remove:
                    for key in product_to_remove:
                        self.product_in_shop.pop(key)
                    print("\nProduct removed successfully")
                else:
                    print("Product not found")
            else:
                break

    def view_product(self):
        print("------------------------------------------------------------------")
        for x, y in self.product_in_shop.items():
            print(x, y)
        print("------------------------------------------------------------------")

    def investment(self):
        investment = 0
        print("------------------------------------------------------------------")
        for x, y in self.product_in_shop.items():
            investment += x * 0.80

        print(f"Total Amount of investment: {investment}")
        print("------------------------------------------------------------------")

    def profit(self):
        profit = 0
        print("------------------------------------------------------------------")
        for x, y in self.product_in_shop.items():
            profit += x * 0.20

        print(f"Total Amount of profit: {profit}")
        print("------------------------------------------------------------------")

    def customer_visited(self):
        print(f"Total number of customers visited: {Customer.customer_visited}")

    def record_expenses(self):
        type_of_expense = input("Enter the type of expense: ")
        money = int(input("Enter how much you spent: "))
        self.expenses.update({type_of_expense: money})
        print(self.expenses)


class Customer:
    customer_visited = 0
    cart = {}
    total_bill=0
    def __init__(self):
        Customer.customer_visited += 1

    def add_product_to_cart(self):
        print("----------------------------------------------------------")
        print("      Products available in the shop right now:")
        for price, product in Owner.product_in_shop.items():
            print(price, product)
        print("----------------------------------------------------------")
        while True:
            z = int(input("Enter 1 to add Product and 2 to stop adding product: "))
            if z == 1:
                product = input("Enter Product to be added: ")
                product_to_added = []

                for key, value in Owner.product_in_shop.items():
                    if value == product:
                        product_to_added.append((key, value))

                if product_to_added:
                    for key, value in product_to_added:
                        self.cart.update({key: value})
                    print("\nProduct added successfully")
                else:
                    print("\nProduct not found")
            else:
                break

    def remove_product_from_cart(self):
        while True:
            z = int(input("Enter 1 to remove Product and 2 to stop removing product: "))
            if z == 1:
                product = input("Enter Product to be removed: ")
                product_to_remove = []

                for key, value in self.cart.items():
                    if value == product:
                        product_to_remove.append(key)

                if product_to_remove:
                    for key in product_to_remove:
                        self.cart.pop(key)
                    print("\nProduct removed successfully")
                else:
                    print("\nProduct not found")
            else:
                break

    def view_cart(self):
        for price, product in self.cart.items():
            print(price, product)
    
    def billing(self):
        self.total_bill = sum(self.cart.keys())
        print(f"Total bill: {self.total_bill}")

        payment_method = input("Select Payment Method (cash): ")
        if payment_method.lower() == "cash":
            self.pay_cash(self.total_bill)
        else:
            print("Invalid payment method.")
            
    def pay_cash(self, amount):
        # Implement cash payment logic here
        print("Payment by cash.")
        amount=int(input("Enter amount"))
        if amount>=self.total_bill:
            print("payment sucessfull")
            change=amount-self.total_bill
            print("change ",change)
            
            
            
            # text-file bill 
            with open("bill.txt", "w") as file:
                file.write("Receipt:\n")
                file.write("--------------------------------------------------\n")
                file.write("Items in Cart:\n")
                for price, product in self.cart.items():
                    file.write(f"{product}: {price}\n")
                file.write("--------------------------------------------------\n")
                file.write(f"Total bill: {self.total_bill}\n")
                file.write(f"Amount paid: {amount}\n")
                file.write(f"Change: {change}\n")
                file.write("--------------------------------------------------\n")
        else:
            print("Insufficent cash")
            
            
            print()
            print("You have to payment process again")
            self.billing()


class Shop:
    while True:
        print("-------------------- Welcome To Dukaan Wala --------------------")
        print("       Who are you?")
        print("       1 ==> Owner")
        print("       2 ==> Customer")
        print("       3 ==> Exit")

        choice = int(input("Enter Your choice: "))

        if choice == 1:
            print("   *****   Welcome Owner   ***** \n")
            obj = Owner()
            user = "Shop@123"
            software_password = "12345678"
            user_name = input("Enter User Name: ")
            password = input("Enter Password: ")
            while True:
                if user_name == user and software_password == password:
                    print("Login Successfully \n")
                    while True:
                        browsing = int(input("1 ==> Add products\n2 ==> Remove products\n3 ==> View products\n"
                                             "4 ==> Investment\n5 ==> Profit\n6 ==> Record expenses\n"
                                             "7 ==> Customers visited\n8 ==> Exit\n"))
                        if browsing == 1:
                            obj.add_product()
                        elif browsing == 2:
                            obj.remove_product()
                        elif browsing == 3:
                            obj.view_product()
                        elif browsing == 4:
                            obj.investment()
                        elif browsing == 5:
                            obj.profit()
                        elif browsing == 6:
                            obj.record_expenses()
                        elif browsing == 7:
                            obj.customer_visited()
                        else:
                            break
                    break
                else:
                    print("Wrong username or password\n")
                    break

        elif choice == 2:
            print("    *****  Welcome To Dukaan Wala  ***** \n")
            obj = Customer()
            while True:
                browsing = int(input("1 ==> Add products to cart\n2 ==> Remove products from cart\n"
                                     "3 ==> View cart\n4 ==> Billing\n5 ==> Exit\n"))
                if browsing == 1:
                    obj.add_product_to_cart()
                elif browsing == 2:
                    obj.remove_product_from_cart()
                elif browsing == 3:
                    obj.view_cart()
                elif browsing == 4:
                    obj.billing()
                    break
                else:
                    break

        else:
            break
