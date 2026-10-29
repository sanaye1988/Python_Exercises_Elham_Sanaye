class Product:  
       
    products_list = []
    
    def __init__(self,name,price,quantity,category):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category
        
             
        
    def __str__(self):
        return f'{self.name} : {self.category}'
        
        
    def update_price(self,price):
        if price < 0:
            raise ValueError('price can not be negative!!')
         
        self.price = price
        return price
 
    
    def add_stock(self,stock):
        if stock < 0:
            raise ValueError('stock can not be negative!!')
        new_quantity = self.quantity + stock
        return new_quantity
    
    
    def sell(self,stock):
        if stock < 0:
            raise ValueError('stock can not be negative!!')
        elif stock > self.quantity:
            raise ValueError('quantity is not available!!')
        else:    
            new_quantity = self.quantity - stock
            return new_quantity
    
    
    def apply_discount(self,discount):
        if 0 < discount < 100:
            new_price = self.price - self.price * discount/100
            return new_price        
        else:
            raise ValueError('discount is not correct!!')
    
    def total_value(self):
        total_value = self.price * self.quantity
        return total_value
    

'''
    def find_max_total_value(self):
        products_list = []
        total_value = self.price * self.quantity
        products_list.append(total_value)
        max_total_value = max(products_list)
        for total_value in products_list:
            if total_value > max_total_value:
                max_total_value = total_value
                return max_total_value
      
'''

p1 = Product('iphone 13', 1500, 3, 'electronics')
print(p1)

p2 = Product('iphone 18', 2500, 5, 'electronics')
print(p2)

p3 = Product('airpods', 1000, 4, 'electronics')
print(p3)


p1.products_list.append(p1)
p1.products_list.append(p2)
p1.products_list.append(p3)
print(Product.products_list)

    

p1.quantity

p1.update_price(1300)
p1.add_stock(4)
p1.sell(1)
p1.apply_discount(10)
p1.total_value()



    