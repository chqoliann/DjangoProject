"""
#1
from datetime import datetime, timedelta

class Patient:
    def __init__(self, name, surname, age, gender):
        self.name = name
        self.surname = surname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"{self.name} {self.surname} - {self.gender}, {self.age} years old."

    def __ne__(self, other):
        return not self.__eq__(other)


class Doctor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.schedule = {}

    def __repr__(self):
        schedule_str = "\n".join([f"{dt}: {patient}" for dt, patient in self.schedule.items()])
        return f"Doctor {self.name} {self.surname} schedule:\n{schedule_str}"

    def register_patient(self, patient, appointment_datetime):
        if not self.is_registered(patient):
            if self.is_free(appointment_datetime):
                self.schedule[appointment_datetime] = patient
                print(f"Patient {patient} successfully registered at {appointment_datetime}.")
            else:
                print(f"Datetime {appointment_datetime} already taken by {self.schedule[appointment_datetime]} patient.")
        else:
            print(f"Patient {patient} is already registered.")

    def is_free(self, appointment_datetime):
        end_time = appointment_datetime + timedelta(minutes=30)
        for dt, patient in self.schedule.items():
            if appointment_datetime < dt < end_time or dt < appointment_datetime < end_time:
                return False
        return True

    def is_registered(self, patient):
        return patient in self.schedule.values()


patient1 = Patient("John", "Doe", 30, "M")
doctor1 = Doctor("Alice", "Smith")
appointment_datetime1 = datetime(2024, 1, 26, 9, 0)
doctor1.register_patient(patient1, appointment_datetime1)
print(doctor1)

patient2 = Patient("Jane", "Doe", 25, "F")
doctor1.register_patient(patient2, appointment_datetime1)
print(doctor1)
"""
"""
#2
class Product:
    def __init__(self, price, id, quantity):
        self.price = price
        self.id = id
        self.quantity = quantity

    def __repr__(self):
        return f"Product(id={self.id}, price={self.price}, quantity={self.quantity})"

    def buy(self, count):
        if count > self.quantity:
            raise ValueError("Not enough quantity available for purchase.")
        self.quantity -= count

    @classmethod
    def get_by_id(cls, products, product_id):
        for product in products:
            if product.id == product_id:
                return product
        return None


class Inventory:
    def __init__(self):
        self.products = []

    def __repr__(self):
        return f"Inventory(products={self.products})"

    def add_product(self, product):
        self.products.append(product)

    def sum_of_products(self):
        total_value = 0
        for product in self.products:
            total_value += product.price * product.quantity
        return total_value



product1 = Product(price=10, id=1, quantity=20)
product2 = Product(price=15, id=2, quantity=15)
product3 = Product(price=5, id=3, quantity=30)

inventory = Inventory()

inventory.add_product(product1)
inventory.add_product(product2)
inventory.add_product(product3)

try:
    product2.buy(10)
    product3.buy(25)
except ValueError as e:
    print(f"Error: {e}")

print("Updated Inventory:", inventory)
print("Sum of Products in Inventory:", inventory.sum_of_products())
"""
"""
#3
class Passenger:
    def __init__(self, name, city, room_type, room_count):
        self.name = name
        self.city = city
        self.room_type = room_type
        self.room_count = room_count

    def __repr__(self):
        return f"Passenger(name={self.name}, city={self.city}, Room_type={self.room_type}, Room_count={self.room_count})"

    def get_name(self):
        return self.name

    def get_city(self):
        return self.city

    def get_room_type(self):
        return self.room_type

    def get_room_count(self):
        return self.room_count


class Hotel:
    def __init__(self, city, rooms):
        self.city = city
        self.rooms = rooms

    def __repr__(self):
        return f"Hotel(city={self.city}, rooms={self.rooms})"

    def get_city(self):
        return self.city

    def free_rooms_list(self):
        return self.rooms

    def reserve_rooms(self, room_type, count):
        if room_type in self.rooms and self.rooms[room_type] >= count:
            self.rooms[room_type] -= count
            print(f"Reservation successful: {count} {room_type} room(s) booked.")
        else:
            print(f"Sorry, not enough available {room_type} room(s) for your request.")



if __name__ == "__main__":
    hotel_rooms = {
        'penthouse': 3,
        'single': 10,
        'double': 7
    }

    hotel1 = Hotel(city="ExampleCity", rooms=hotel_rooms)

    passenger1 = Passenger(name="John Doe", city="ExampleCity", room_type="single", room_count=2)
    print(passenger1)

    print("\nBefore Reservation:")
    print(hotel1.free_rooms_list())

    hotel1.reserve_rooms(passenger1.get_room_type(), passenger1.get_room_count())

    print("\nAfter Reservation:")
    print(hotel1.free_rooms_list())
"""



