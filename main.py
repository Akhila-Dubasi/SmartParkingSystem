from Vehicle import Bike, Car, SUV, Truck
from payment import CashPayment, CardPayment, UPIPayment
from parking_system import ParkingSpot, ParkingLot
def create_parking_lot():
    lot=ParkingLot()
    lot.add_spot(ParkingSpot(1, 'S'))
    lot.add_spot(ParkingSpot(2, 'M'))
    lot.add_spot(ParkingSpot(3, 'L'))
    lot.add_spot(ParkingSpot(4, 'XL'))
    return lot
def main_menu():
    parking_lot=create_parking_lot()
    while True:
        print("\nParking Management System")
        print("1.Park a Vehicle")
        print("2.Unpark a Vehicle")
        print("3.Show Parking Lot Status")
        print("4.Exit")
        choice=input("Enter your choice: ")
        if choice=='1':
            park_vehicle_flow(parking_lot)
        elif choice=='2':
            unpark_vehicle_flow(parking_lot)
        elif choice=='3':
            parking_lot.show_spots()
        elif choice=='4':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
def park_vehicle_flow(parking_lot):
    print("\nPark a Vehicle")
    v_type=input("Enter vehicle type (bike/car/suv/truck): ").strip().lower()
    plateno=input("Enter vehicle plate number: ").strip()
    owner_name=input("Enter owner's name: ").strip()
    vehicle=None
    if v_type=='bike':
        helmet=input("Is a helmet required? (yes/no): ").strip().lower() == 'yes'
        vehicle=Bike(plateno, owner_name, helmet)
    elif v_type=='car':
        seats=int(input("Enter number of seats: "))
        vehicle=Car(plateno, owner_name, seats)
    elif v_type=='suv':
        four_wheel_drive=input("Is it 4WD? (yes/no): ").strip().lower() == 'yes'
        vehicle=SUV(plateno, owner_name, four_wheel_drive)
    elif v_type=='truck':
        load=int(input("Enter max load capacity (tons): "))
        vehicle=Truck(plateno, owner_name, load)
    else:
        print("Invalid vehicle type.")
        return
    parking_lot.park_vehicle(vehicle)
def unpark_vehicle_flow(parking_lot):
    print("\n--- Unpark a Vehicle ---")
    plateno=input("Enter the plate number of the vehicle to unpark: ").strip()
    try:
        hours=float(input("Enter parking duration in hours: "))
    except ValueError:
        print("Invalid duration. Please enter a number.")
        return
    fee=parking_lot.unpark_vehicle(plateno, hours)
    if fee>0:
        method=input("Choose payment method (cash/card/upi): ").strip().lower()
        if method=='cash':
            payment=CashPayment()
        elif method=='card':
            payment=CardPayment()
        elif method=='upi':
            payment=UPIPayment()
        else:
            print("Invalid payment method.")
            return
        payment.process_payment(fee)
if __name__ == "__main__":
    main_menu()