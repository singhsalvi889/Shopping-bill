
from abc import ABC, abstractmethod

class Passenger(ABC):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def get_discount(self):
        pass

class RegularPassenger(Passenger):
    def get_discount(self):
        return 0


class StudentPassenger(Passenger):
    def get_discount(self):
        return 10


class Flight:
    def __init__(self, code, airline, source, destination, seats, fare):
        self.code = code
        self.airline = airline
        self.source = source
        self.destination = destination
        self.__seats = seats
        self.fare = fare

    def display(self):
        print(f"{self.code} | {self.airline} | "
              f"{self.source} to {self.destination} | "
              f"Seats: {self.__seats} | Fare: Rs.{self.fare}")

    def get_seats(self):
        return self.__seats

    def book_seats(self, count):
        if count <= self.__seats:
            self.__seats -= count
            return True
        return False


class Booking:
    def __init__(self, booking_id, flight, passenger, tickets, subtotal, discount):
        self.booking_id = booking_id
        self.flight = flight
        self.passenger = passenger
        self.tickets = tickets
        self.subtotal = subtotal
        self.discount = discount
        self.total = subtotal - discount

    def display_summary(self):
        print("\n----- BOOKING SUMMARY -----")
        print("Booking ID:", self.booking_id)
        print("Flight:", self.flight.code)
        print("Route:", self.flight.source, "to", self.flight.destination)
        print("Passenger:", self.passenger.name)
        print("Age:", self.passenger.age)
        print("Passenger Type:", type(self.passenger).__name__)
        print("Tickets:", self.tickets)
        print("Base Fare:", self.flight.fare)
        print("Subtotal: Rs.", self.subtotal)
        print("Discount: Rs.", self.discount)
        print("Final Amount: Rs.", self.total)
        print("Booking confirmed!")


# Main booking system
class FlightBookingSystem:
    def __init__(self):
        self.flights = [
            Flight("PN101", "Kiran Air", "Pune", "Delhi", 20, 4000),
            Flight("MB102", "Sky Air", "Mumbai", "Bengaluru", 15, 3500),
            Flight("PN103", "Air India", "Pune", "Hyderabad", 25, 3000)
        ]
        self.bookings = []
        self.next_id = 1001

    def display_flights(self):
        print("\n----- AVAILABLE FLIGHTS -----")
        for flight in self.flights:
            flight.display()

    def find_flight(self, code):
        for flight in self.flights:
            if flight.code.lower() == code.lower():
                return flight
        return None

    def book_flight(self):
        code = input("Enter flight code: ").strip()
        flight = self.find_flight(code)

        if flight is None:
            print("Error: Invalid flight code.")
            return

        name = input("Enter passenger name: ").strip()
        if not name:
            print("Error: Name cannot be blank.")
            return

        try:
            age = int(input("Enter age: "))
            if age <= 0:
                print("Error: Age must be greater than 0.")
                return

            passenger_type = input(
                "Passenger type (Regular/Student): "
            ).strip().lower()

            if passenger_type == "regular":
                passenger = RegularPassenger(name, age)
            elif passenger_type == "student":
                passenger = StudentPassenger(name, age)
            else:
                print("Error: Choose Regular or Student.")
                return

            tickets = int(input("Enter number of tickets: "))
            if tickets <= 0:
                print("Error: Tickets must be greater than 0.")
                return

        except ValueError:
            print("Error: Please enter valid numbers.")
            return

        if tickets > flight.get_seats():
            print("Booking failed: Not enough seats available.")
            return

        # Calculate fare
        subtotal = flight.fare * tickets
        discount = subtotal * passenger.get_discount() / 100

        # Confirm booking only after validation
        flight.book_seats(tickets)

        booking = Booking(
            "BK" + str(self.next_id),
            flight,
            passenger,
            tickets,
            subtotal,
            discount
        )

        self.bookings.append(booking)
        self.next_id += 1
        booking.display_summary()

    def view_booking(self):
        if not self.bookings:
            print("No booking available.")
        else:
            self.bookings[-1].display_summary()

    def run(self):
        while True:
            print("\n===== KIRAN AIR BOOKING =====")
            print("1. View Flights")
            print("2. Book Flight")
            print("3. View Booking")
            print("4. Exit")

            choice = input("Enter choice: ").strip()

            if choice == "1":
                self.display_flights()
            elif choice == "2":
                self.book_flight()
            elif choice == "3":
                self.view_booking()
            elif choice == "4":
                print("Thank you for using Kiran Air Booking!")
                break
            else:
                print("Invalid choice. Please try again.")

system = FlightBookingSystem()
system.run()
