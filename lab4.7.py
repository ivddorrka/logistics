"""
Logistic  System
"""
import random 

class Item:
    """
    For item and it's price
    """
    def __init__(self, name, price):
        """Init function"""
        self.name = name
        self.price = price
    def __str__(self):
        """For an output for furhter use
        >>> print(Item('book', 44).__str__())
        book, 44
        """
        return f'{self.name}, {self.price}'

class Location:
    """For user's location"""
    def __init__(self, city, postoffice):
        """Init function"""
        self.city = city
        self.postoffice = postoffice
    

class Vehicle:
    """To track vehicles"""
    def __init__(self, vehicleNo):
        """Init function"""
        self.vehicleNo = vehicleNo
        self.isAvailable = True
    def __str__(self):
        return f'{self.vehicleNo}, {self.isAvailable}'


class Order:
    """To make orders"""
    def __init__(self, user_name, city, postoffice, items):
        self.user_name = user_name
        self.city = city
        self.items = items
        self.postoffice = postoffice
        self.id_here = random.randint(10000, 100000)
    def __str__(self):
        """For output"""
        return f'Your order number is {self.id_here}'
    def calculateAmount(self):
        """To calculate the result sum of an order"""
        sum_1 = [float(str(i).split(', ')[1]) for i in self.items]
        return sum(sum_1)
    def assignVehicle(self, vehicle):
        """To assign vehcle if one is available"""
        vehicle.isAvailable = False

class LogisticsSystem:
    """The main class to place and track orders"""
    def __init__(self,vehicles):
        """Init function"""
        self.vehicles = vehicles
        self.ord = []
    def placeOrder(self, my_order):
        """To assign vehicle and add an order to a list"""
        res = []
        for i in self.vehicles:
            if i.isAvailable == True:
                my_order.assignVehicle(i)
                self.ord.append(my_order)
                res.append(i.__str__())
                break
        if len(res) == 0:
            return "There is no available vehicle to deliver an order."
    def trackOrder(self, id_num):
        """For user to track orders"""
        for i in self.ord:
            if i.id_here == id_num:
                return f"Your order #{id_num} is sent to {i.city}. Total price: {i.calculateAmount()} UAH."
        return 'No such order.'


if __name__ == "__main__":
    vehicles = [Vehicle(1), Vehicle(2)]
    LogSystem = LogisticsSystem(vehicles)
    my_items = [Item('book',110), Item('chupachups',44)]
    my_order = Order(user_name = 'Oleg', city = 'Lviv', postoffice = 53, items = my_items)
    num = my_order.id_here
    LogSystem.placeOrder(my_order)
    print(LogSystem.trackOrder(num))
    my_items2 = [Item('flowers',11), Item('shoes',153), Item('helicopter',0.33)]
    my_order2 = Order('Andrii', 'Odessa', 3, my_items2)
    num_2 = my_order2.id_here
    LogSystem.placeOrder(my_order2)
    print(LogSystem.trackOrder(num_2))

    my_items3 = [Item('coat',61.8), Item('shower',5070), Item('rollers',700)]

    my_order3 = Order('Olesya', 'Kharkiv', 17, my_items3)
    num_3 = my_order3.id_here

    print(LogSystem.placeOrder(my_order3))
    print(LogSystem.trackOrder(num_3))