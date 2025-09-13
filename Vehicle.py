from abc import ABC,abstractmethod
class Vehicle(ABC):
    def __init__(self,plateno,name):
        self.__plateno=plateno
        self.__name=name
    def get_plateno(self):
        return self.__plateno
    def get_name(self):
        return self.__name
    def set_name(self,name):
        self.__name=name
    @abstractmethod
    def display(self):
        pass
    @abstractmethod
    def calculate_parking_fee(self,hours):
        pass
class Bike(Vehicle):
    def __init__(self,plateno,name,helmet_required):
        super().__init__(plateno,name)
        self.helmet_required=helmet_required
    def display(self):
        print(f"Bike - License: {self.get_plateno()}, Owner: {self.get_name()}, Helmet Required: {self.helmet_required}")
    def calculate_parking_fee(self,hours):
        return 20*hours
class Car(Vehicle):
    def __init__(self,plateno,name,seats):
        super().__init__(plateno, name)
        self.seats=seats
    def display(self):
        print(f"Car - License: {self.get_plateno()}, Owner: {self.get_name()}, Seats: {self.seats}")
    def calculate_parking_fee(self,hours):
        return 50*hours
class SUV(Vehicle):
    def __init__(self,plateno,name,four_wheel_drive):
        super().__init__(plateno,name)
        self.four_wheel_drive=four_wheel_drive
    def display(self):
        print(f"SUV - License: {self.get_plateno()}, Owner: {self.get_name()}, 4WD: {self.four_wheel_drive}")
    def calculate_parking_fee(self,hours):
        return 70*hours
class Truck(Vehicle):
    def __init__(self,plateno,name,max_load_capacity):
        super().__init__(plateno,name)
        self.max_load_capacity=max_load_capacity
    def display(self):
        print(f"Truck - License: {self.get_plateno()}, Owner: {self.get_name()}, Max Load: {self.max_load_capacity} tons")
    def calculate_parking_fee(self,hours):
        return 100*hours