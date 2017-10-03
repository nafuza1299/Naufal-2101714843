def Cash():
    list1 = []
    list2 = []
    list3 = []
    message2 = "\nFinal Total:" + " " + "RP"
    class Cashier():
        """Welcome, How may I help you?"""

        def __init__(self, item, price, amt):
            """"Declaring item and its price."""
            self.item = item
            self.price = price
            self.amt = amt

        def buy(self):
            """"Buying an item"""
            print("\nBuying " + self.item.title())
            print("Price: " + "RP " + str(self.price))
            for l in range(1):
                if self.price != self.price:
                    break
                else:
                    continue
            list1.append(self.item)
            list2.append(self.price)
            fin = self.price * self.amt
            print("Total Price: " + "RP " + str(fin))
            list3.append(fin)
                    #sfin0 = str(fin0)
                    #total.append(sfin0)

    n = int(input("How many items are you buying? "))
    if n == 0:
            print("Thank You for your visit!")
            return False
    for i in range(n):
        the_cashier = Cashier(str(input("\nWhat are you buying? ").title()), int(input("What is the price tag?")), int(input("Amount: ")))
        the_cashier.buy()
    print('\nPurchasing: ')
    for x in list1:
        print(x)
    final = [int(i) for i in list3]
    print(message2, sum(final))
    is_that_it = str(input("\nAnything Else? (Yes/No)")).title().strip()
    for t in range(1):
        if is_that_it == "Yes":
            return Cash()
        else:
            return False
Cash()
