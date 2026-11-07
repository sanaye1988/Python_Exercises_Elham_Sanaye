class Product:
    def __init__(self,code,name,price,stock,sell_count):
        self.code = code
        self.name = name
        self.price = price
        self.stock = stock
        self.sell_count = sell_count
        
        
    def __str__(self):
        print(f'{self.name}:{self.code}')
        
    
    def apply_discount(self,percentage):
        if 0 < percentage <= 100 : 
            self.price -= self.price * percentage / 100
            return self.price
        else:
            print('percentage cannot be negative!')
    
    def restock(self,quantity):
        if quantity > 0:
            self.stock += quantity
            return self.stock
        else:
            print('quantity cannot be negative!')
  
        
    def is_available(self):
        if self.stock > 0 :
            print('stock is enough.')
               
                      
    def sell(self,quantity):
        if quantity <= self.stock :
            self.stock -= quantity
            self.sell_count += quantity
            print(f'{quantity} sold, {self.stock} is available, number of sales is:{self.sell_count}')
        elif quantity <= 0:
            print("quantity cannot be negative!")
        else:
            print("quantity is not correct!")
    
    def show(self):
        print(f'Code: {self.code}')
        print(f'name: {self.name}')
        print(f'price: {self.price}')
        print(f'stock: {self.stock}')
        print(f'sell_count: {self.sell_count}')
        
        
    
import math 

class Location:
    def __init__(self,x,y,address):
        self.x = x
        self.y = y
        self.address = address
        
    
    def calculate_distance(self,other_location):
        if not isinstance(other_location, Location):
            raise NotImplementedError('not implemented!!')

        x_distance = self.x - other_location.x
        y_distance = self.y - other_location.y
        
        distance = math.sqrt(x_distance**2 + y_distance**2)
        return distance



class DigitalProduct(Product):
    def __init__(self, code, name, price, stock, sell_count,download_link):
        super().__init__(code, name, price, stock, sell_count)
        self.download_link = download_link
        
        
    def get_download_link(self):
        return self.download_link
    
    
    
class PhysicalProduct(Product):
    def __init__(self, code, name, price, stock, sell_count,weight,warehouse_location):
        super().__init__(code, name, price, stock, sell_count)
        self.weight = weight
        self.warehouse_location = warehouse_location
        
        
    def calculate_shipping(self,destination):
        if not isinstance(destination, Location):
            raise NotImplementedError('not implemented!!')
        
        distance = destination.calculate_distance(self.warehouse_location)
      
        shipping_cost = distance * self.weight * 1000
    
        return shipping_cost




digitalpr1 = DigitalProduct(
    12, "Python book", 34, 5, 1,
    "https://python_book.com/download")

digitalpr2 = DigitalProduct(
    23, "ai book", 87, 4, 2,
    "https://ai_course.com/download")

physicalpr1 = PhysicalProduct(
    24,
    "Laptop",
    8,
    1000,
    1,
    3,
    Location(35.6892, 51.3890, "Tehran"))

physicalpr2 = PhysicalProduct(
    45,
    "iphone",
    6,
    1500,
    2,
    1,
    Location(36.2605, 59.6168, "Tabriz"))

loc1 = Location(35.6892, 51.3890, "Tehran")
loc2 = Location(36.2605, 59.6168, "Tabriz")



loc1.calculate_distance(loc2)

digitalpr1.get_download_link()

physicalpr2.calculate_shipping(Location(36.2605, 59.6168, "Tabriz"))

