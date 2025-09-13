from Vehicle import Bike, Car, SUV, Truck
from payment import Payment, CashPayment, CardPayment, UPIPayment # Import the new payment classes
class ParkingSpot:
    def __init__(self,spot_id,size):
        self.spot_id=spot_id
        self.size=size
        self.__occupied=False
        self.__vehicle=None
    def get_status(self):
        return "Occupied" if self.__occupied else "Available"
    def get_vehicle(self):
        return self.__vehicle
    def assign_vehicle(self, vehicle):
        type_map={
            Bike:['S', 'M', 'L', 'XL'],
            Car:['M', 'L', 'XL'],
            SUV:['L', 'XL'],
            Truck:['XL']
        }
        if type(vehicle) in type_map:
            if self.size in type_map[type(vehicle)]:
                if not self.__occupied:
                    self.__vehicle=vehicle
                    self.__occupied=True
                    print(f"Vehicle {vehicle.get_plateno()} parked in spot {self.spot_id}")
                    return True
                else:
                    print(f"Spot {self.spot_id} already occupied")
                    return False
            else:
                print(f"Vehicle type does not fit spot {self.spot_id}")
                return False
        print("Invalid vehicle type.")
        return False
    def remove_vehicle(self):
        if self.__occupied:
            vehicle=self.__vehicle
            self.__vehicle=None
            self.__occupied=False
            print(f"Vehicle {vehicle.get_plateno()} removed from spot {self.spot_id}")
            return vehicle
        else:
            print(f"No vehicle to remove in spot {self.spot_id}")
            return None
    def show_spot(self):
        status=self.get_status()
        print(f"Spot ID: {self.spot_id},Size: {self.size},Status: {status}")
        if self.__occupied:
            print(f"Parked Vehicle: {self.__vehicle.get_plateno()} ({self.__vehicle.get_name()})")
class ParkingLot:
    def __init__(self):
        self.spots=[]
    def add_spot(self,spot):
        self.spots.append(spot)
    def show_spots(self):
        for spot in self.spots:
            spot.show_spot()
    def park_vehicle(self,vehicle):
        for spot in self.spots:
            if spot.assign_vehicle(vehicle):
                return
        print(f"No suitable spot available for vehicle {vehicle.get_plateno()}")
    def unpark_vehicle(self,plateno,hours):
        for spot in self.spots:
            if spot.get_vehicle() and spot.get_vehicle().get_plateno()==plateno:
                vehicle_to_unpark=spot.remove_vehicle()
                fee=vehicle_to_unpark.calculate_parking_fee(hours)
                print(f"Parking Fee for {plateno}: ₹{fee:.2f}")
                return fee
        print(f"Vehicle with plate number {plateno} not found in the parking lot.")
        return 0