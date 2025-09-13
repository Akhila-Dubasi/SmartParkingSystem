from abc import ABC, abstractmethod
class Payment(ABC):
    @abstractmethod
    def process_payment(self, amount):
        pass
class CashPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount:.2f} via Cash")
class CardPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount:.2f} via Card")
class UPIPayment(Payment):
    def process_payment(self, amount):
        print(f"Paid ₹{amount:.2f} via UPI")