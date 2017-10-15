class menu:
    def __init__(self, foodcode):
       self.foodcode = foodcode

class food(menu):
    def __init__(self):
        super(food, self).__init__(1)
        self.pricefood= {"Chicken Terayaki" : 35000, "Sushi Set" : 40000}
class food1(menu):
    def __init__(self):
        super(food1,self). __init__(2)
class drink(menu):
    def __init__(self):
        super(drink, self).__init__(3)
class drink1(menu):
    def __init__(self):
        super(drink1,self).__init__(4)