class Bus:
    def __init__(self, route_number, destination, drive_method):
        self.route_number = route_number
        self.destination = destination
        self.drive_method = drive_method
        self.passengers = []

# return how many passengers are on the bus
    def amount_of_passengers(self, passengers):
        return len(self.passengers)

# take a person and append it to the passenger list
    def pick_up(self, passenger_to_pick_up):
        self.passengers.append(passenger_to_pick_up)
    
# drop off a passenger and remove them from the list
    def drop_off(self, passenger_to_drop_off):
        return self.passengers.remove(passenger_to_drop_off)
    
# remove all of the passengers
# when the bus reaches the destination
# or the bus breaks down
    def remove_all_passengers(self):
        self.passengers.clear()
        
    def pick_up_from_stop(self, bus_stop):
        for passenger in bus_stop.queue:
            self.pick_up(passenger)
        bus_stop.clear()