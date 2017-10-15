from resmodule import food,food1,drink,drink1
class japanese_restaurant:
    def __init__(self,tax,service_fee ):
        self.tax=tax
        self.service_fee = service_fee
        self.amountfood = {"Chicken Terayaki": 0, "Sushi Set": 0}
        self.amountdrink = {"Ice Lemon Tea": 0, "Blackcurrent": 0}
        self.rev = 0
        self.stock = 100
        self.food = {"Chicken Terayaki" : self.stock, "Sushi Set" : self.stock}
        self.drink = {"Ice Lemon Tea": self.stock, "Blackcurrent": self.stock}
        self.pricefood= {"Chicken Terayaki" : 35000, "Sushi Set" : 40000}
        self.pricedrink = {"Ice Lemon Tea": 10000, "Blackcurrent": 11000}
        self.food_data={}
        self.acc = 0

    def food_database(self):
        self.food_data={}
        self.food_data["amountmenu"]=self.amountfood
        self.food_data["amountmenu"]=self.amountdrink
        self.food_data["revenue"]=self.rev
        self.food_data["stock"]=self.stock
        self.food_data["total"]=self.acc

    def stock1(self, menu):
        if isinstance(menu, food):
            self.food["Chicken Terayaki"]-=1
        elif isinstance(menu,food1):
            self.food["Sushi Set"]-=1
        elif isinstance(menu, drink):
            self.drink["Ice Lemon Tea"]-=1
        elif isinstance(menu,drink1):
            self.drink["Blackcurrent"]-=1

    def order(self, menu):
        if isinstance(menu, food):
            self.rev+=self.pricefood["Chicken Terayaki"]
            return self.pricefood["Chicken Terayaki"]
        elif isinstance(menu,food1):
            self.rev+=self.pricefood["Sushi Set"]
            return self.pricefood["Sushi Set"]
        if isinstance(menu, drink):
            self.rev+=self.pricedrink["Ice Lemon Tea"]
            return self.pricedrink["Ice Lemon Tea"]
        elif isinstance(menu,drink1):
            self.rev+=self.pricedrink["Blackcurrent"]
            return self.pricedrink["Blackcurrent"]

    def amountmenu(self,menu):
        if isinstance(menu,food):
            self.amountfood["Chicken Terayaki"]+=1
        elif isinstance(menu, food1):
            self.amountfood["Sushi Set"]+=1
        elif isinstance(menu,drink):
            self.amountdrink["Ice Lemon Tea"]+=1
        elif isinstance(menu, drink1):
            self.amountdrink["Blackcurrent"]+=1

    def amountmenu_amount(self):
        return self.amountfood["Chicken Terayaki"],self.amountfood["Sushi Set"], self.amountdrink["Ice Lemon Tea"],self.amountdrink["Blackcurrent"],

    def revfee(self):
        return self.rev

    def revfeetax(self):
        self.total = (self.rev*self.tax)+self.service_fee
        return self.total


    def stockremain(self):
        return self.food["Chicken Terayaki"],self.food["Sushi Set"], self.drink["Ice Lemon Tea"], self.drink["Blackcurrent"]
def titlescreen():
    while True:
        Ichiban = japanese_restaurant(1.05, 5000)
        print("Welcome to Ichiban Sushi!")
        tables = int(input("How many people are there?"))
        if tables == 0:
            print("Thank you for coming!")
            return False
        elif tables <=2:
            print("==============================")
            print("          Table of 2          ")
            print("==============================")

        elif tables <=4:
            print("==============================")
            print("          Table of 4          ")
            print("==============================")
        elif tables >=5:
            print("==============================")
            print("          Table of 8          ")
            print("==============================")
        if tables == 1:
            print("Serving", tables, "person")
        if tables > 1:
            print("Serving", tables, "people")
        print("Serving", tables, "people")
        print("\n============================")
        print("            Menu             ")
        print("============================")

        while True:
            print("1.Chicken Terayaki (RP " + str(Ichiban.pricefood["Chicken Terayaki"])+")")
            print("2.Sushi Set (RP " + str(Ichiban.pricefood["Sushi Set"])+")")
            print("3.Ice Lemon Tea (RP " + str(Ichiban.pricedrink["Ice Lemon Tea"])+")")
            print("4.Blackcurrent (RP " + str(Ichiban.pricedrink["Blackcurrent"])+")")
            buy = int(input("What would you like to buy?"))
            if buy == 1:
                classification = food()
            elif buy==2:
                classification=food1()
            elif buy==4:
                classification=drink1()
            else:
                classification = drink()
            payment = Ichiban.order(classification)
            order = Ichiban.amountmenu(classification)
            stockcall = Ichiban.stock1(classification)
            print("\nFee: %d" % payment)
            decision = input("Is there any thing else you would like to order (Y/N)?").title().strip()
            if decision == "N":
                message = ("\nOrdering: \nChicken Terayaki: %d \nSushi Set: %d \nIce Lemon Tea: %d \nBlackcurrent: %d" % Ichiban.amountmenu_amount())
                message1 = message.replace("0", " ")
                print(message1)
                rev = Ichiban.revfee()
                finalrev = Ichiban.revfeetax()
                print("\nTotal Fee: RP " + str(rev))
                print("Total Fee after Tax: RP " + str(finalrev))
                print("\n======================")
                print("   Restaurant Status  ")
                print("======================")
                print("Stock Remaining: \nChicken Terayki:%d \nSushi Set:%d \nIce Lemon Tea:%d \nBlackcurrent: %d" % Ichiban.stockremain())
                print("Profit: RP " + str(finalrev))
                break
        inp_dec = input("Do you want to close the store?N/Y")
        if inp_dec.upper() == "Y":
            return False


titlescreen()
