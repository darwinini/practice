

# Defining a Flight class

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passangers = []

    # method to add passanger to the flight
    def add_passangers(self, name):
        if not self.open_seats(): # similar to if self.open_seats() == 0
            return False
        # otherwise if there are open seats we can append the new passangers
        # for this, we don't need to say else
        self.passangers.append(name)
        return True

    # how many open seats there are
    def open_seats(self):
        return self.capacity - len(self.passangers)

flight = Flight(3)

people = ["Cosette", "Ethan", "Annaliese", "Julie"]

for person in people:
    success = flight.add_passangers(person)
    if success:
        print(f"Added {person} successfully")
    else:
        print(f"No available seats for {person}")
