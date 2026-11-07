class Vehicle:
    def __init__(self,year,model,brand,distance_traveled):
        self.year = year
        self.model = model
        self.brand = brand
        self.distance_traveled = distance_traveled
        
        
    def show_info(self):
        print(f'year of production:{self.year}')
        print(f'model of vehicle:{self.model}')
        print(f'brand of vehicle:{self.brand}')
        print(f'distance traveled is:{self.distance_traveled}')
        
        
        
    def drive(self,distance):
        if distance >= 0:
            self.distance_traveled += distance
            return self.distance_traveled
        else:
            raise ValueError('distance cannot be negative!')
            
            
    def calculate_trip_cost(self,distance):
        raise NotImplementedError('This method is implemented in the child class!')    


     
class GasCar(Vehicle):
    def __init__(self,year,model,brand,distance_traveled,fuel_consumption,fuel_price):
        super().__init__(year, model, brand, distance_traveled)
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        
    def calculate_trip_cost(self,distance):
        trip_cost = distance * self.fuel_consumption * self.fuel_price / 100
        return trip_cost
    
    

class ElectricCar(Vehicle):
    def __init__(self,year,model,brand,distance_traveled,energy_consumption,electricity_price):
        super().__init__(year, model, brand, distance_traveled)
        self.energy_consumption = energy_consumption
        self.electricity_price = electricity_price
    
    
    def calculate_trip_cost(self,distance):
        trip_cost = distance * self.energy_consumption * self.electricity_price / 100
        return trip_cost
    

car1 = GasCar(2020,'rav4','toyota', 50, 8, 3)   
car2 = GasCar(2010,'corolla','toyota', 120, 7, 3)   
car3 = ElectricCar(2014,'model s','tesla', 80,11,5)   
car4 = ElectricCar(2024,'ID4','volkswagen', 100,14,5)  

vehicles = [car1, car2, car3, car4] 

for Vehicle in vehicles:
    Vehicle.show_info()
    print(' ')
    cost = Vehicle.calculate_trip_cost(150)
    print(f'The cost of the trip is:{cost}')
    print('-------------------------')