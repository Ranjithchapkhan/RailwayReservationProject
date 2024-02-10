import random

class RailwayReservationSystem:
    def __init__(self):
        self.users = {} 
        self.trains = {
            1099: {'name': 'Godavari', 'total_seats': 50, 'reserved_seats': []},
            3092: {'name': 'Telangana', 'total_seats': 40, 'reserved_seats': []},
            2452: {'name': 'Tirumala', 'total_seats': 60, 'reserved_seats': []},
            8033: {'name': 'Vande Bharath', 'total_seats': 30, 'reserved_seats': []}
        }

    def create_account(self):
        username = input("Enter username: ")
        password = input("Enter password: ")
        user_id = self.generate_user_id()
        self.users[user_id] = {'username': username, 'password': password}
        print(f"Account created successfully! Your User ID is: {user_id}")

    def generate_user_id(self):
        return random.randint(1000, 9999)

    def generate_pnr(self):
        return random.randint(100000, 999999)

    def display_trains(self):
        print("Available trains:")
        for train_number, details in self.trains.items():
            print(f"Train {train_number} - {details['name']} - Total seats: {details['total_seats']}")

    def book_ticket(self, user_id):
        train_number = int(input("Enter train number: "))
        if train_number not in self.trains:
            print("Invalid train number.")
            return

        total_seats = self.trains[train_number]['total_seats']
        reserved_seats = self.trains[train_number]['reserved_seats']

        if len(reserved_seats) == total_seats:
            print("No available seats on this train.")
            return

        pnr_number = self.generate_pnr()
        reserved_seats.append(pnr_number)
        print(f"Ticket booked successfully! PNR Number: {pnr_number}")

    def cancel_ticket(self, user_id):
        pnr_number = int(input("Enter PNR number to cancel: "))
        for train_number, details in self.trains.items():
            if pnr_number in details['reserved_seats']:
                details['reserved_seats'].remove(pnr_number)
                print("Ticket canceled successfully!")
                return
        print("Invalid PNR number.")

    def display_reserved_seats(self):
        print("Reserved seats:")
        for train_number, details in self.trains.items():
            print(f"Train {train_number} - {details['name']} - Reserved seats: {details['reserved_seats']}")

    def check_pnr_status(self, user_id):
        pnr_number = int(input("Enter PNR number to check status: "))
        for train_number, details in self.trains.items():
            if pnr_number in details['reserved_seats']:
                print(f"PNR Number {pnr_number} is booked on Train {train_number} - {details['name']}.")
                return
        print(f"PNR Number {pnr_number} is not found in the system.")

    def run(self):
        while True:
            print("-"*50,"Railway Reservation System","-"*42)
            print("1. Create Account")
            print("2. Book Ticket")
            print("3. Cancel Ticket")
            print("4. Available Trains")
            print("5. Reserved Seats")
            print("6. Check PNR Status")
            print("7. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                self.create_account()
            elif choice == '2':
                user_id = int(input("Enter your User ID: "))
                self.book_ticket(user_id)
            elif choice == '3':
                user_id = int(input("Enter your User ID: "))
                self.cancel_ticket(user_id)
            elif choice == '4':
                self.display_trains()
            elif choice == '5':
                self.display_reserved_seats()
            elif choice == '6':
                user_id = int(input("Enter your User ID: "))
                self.check_pnr_status(user_id)
            elif choice == '7':
                print("*"*50,"Thank you.Goodbye!","*"*50)
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

if __name__ == "__main__":
    reservation_system = RailwayReservationSystem()
    reservation_system.run()

        