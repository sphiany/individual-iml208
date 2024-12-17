import datetime

# Project Information
print("2023878268")
print("SOFIA HANI BINTI MAZNIZAM")
print("Topic: Flight Booking System")

# Data
flights = "["
{"id": 1, "origin": "Kuala Lumpur", "destination": "Singapore", "date": "2024-12-20", "time": "09:00", "price": 200},
{"id": 2, "origin": "Kuala Lumpur", "destination": "Bangkok", "date": "2024-12-21", "time": "15:00", "price": 350},
{"id": 3, "origin": "Singapore", "destination": "Tokyo", "date": "2024-12-22", "time": "08:00", "price": 1000},
"]"

bookings = []

# Functions
def search_flights(origin, destination, date):
    return [f for f in flights if f['origin'] == origin and f['destination'] == destination and f['date'] == date]

def book_flight(flight_id, name):
    flight = next((f for f in flights if f['id'] == flight_id), None)
    if flight:
        bookings.append({"id": len(bookings) + 1, "flight": flight, "name": name, "price": flight['price']})
        return True
    return False

def view_bookings():
    for b in bookings:
        print(f"ID: {b['id']}, Name: {b['name']}, Flight: {b['flight']['origin']} to {b['flight']['destination']}, Price: {b['price']}")

def update_booking(booking_id, name):
    for b in bookings:
        if b['id'] == booking_id:
            b['name'] = name
            return True
    return False

def delete_booking(booking_id):
    for b in bookings:
        if b['id'] == booking_id:
            bookings.remove(b)
            return True
    return False

def calculate_totals():
    total = sum(b['price'] for b in bookings)
    avg = total / len(bookings) if bookings else 0
    print(f"Total: {total}, Average: {avg:.2f}")

# Menu
def menu():
    while True:
        print("\n--- Menu ---")
        print("1. Search Flights")
        print("2. Book Flight")
        print("3. View Bookings")
        print("4. Update Booking")
        print("5. Delete Booking")
        print("6. Totals and Averages")
        print("7. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            origin = input("Origin: ")
            dest = input("Destination: ")
            date = input("Date (YYYY-MM-DD): ")
            results = search_flights(origin, dest, date)
            if results:
                for r in results:
                    print(f"ID: {r['id']}, Time: {r['time']}, Price: {r['price']}")
            else:
                print("No flights found.")

        elif choice == "2":
            try:
                flight_id = int(input("Flight ID: "))
                name = input("Passenger Name: ")
                if book_flight(flight_id, name):
                    print("Booking successful.")
                else:
                    print("Flight not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "3":
            if bookings:
                view_bookings()
            else:
                print("No bookings available.")

        elif choice == "4":
            try:
                booking_id = int(input("Booking ID: "))
                name = input("New Name: ")
                if update_booking(booking_id, name):
                    print("Booking updated.")
                else:
                    print("Booking not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "5":
            try:
                booking_id = int(input("Booking ID: "))
                if delete_booking(booking_id):
                    print("Booking deleted.")
                else:
                    print("Booking not found.")
            except ValueError:
                print("Invalid input.")

        elif choice == "6":
            calculate_totals()

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")

menu()