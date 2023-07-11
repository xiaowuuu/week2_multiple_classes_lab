from person import Person
from bus import Bus
from bus_stop import BusStop

# person
person_1 = Person("Steven", 34)
person_2 = Person("Laura", 21)
person_3 = Person("Wanda", 58)
person_4 = Person("Patrcik", 30)
person_5 = Person("Marc", 40)

# passengers (option + shift + up arrow to copy lines)
print(f"Name: {person_1.name}, Age: {person_1.age}.")
print(f"Name: {person_2.name}, Age: {person_2.age}.")
print(f"Name: {person_3.name}, Age: {person_3.age}.")
print(f"Name: {person_4.name}, Age: {person_4.age}.")
print(f"Name: {person_5.name}, Age: {person_5.age}.")

# bus
bus = Bus(11, "Leith Walk")
print(f"Bus {bus.route_number} is going to {bus.destination}. Take care of your belongings.")
print(f"Bus {bus.route_number} has left the station. {bus.drive_method()}.")

starting_passenger_count = bus.passenger_count()
print(f"There are {starting_passenger_count} passengers on the bus.")

bus_stop = BusStop("Craigmillar")
print(f"{person_1.name}")
print(f"{bus_stop.name} is wating at {bus.destination} station")


# pick up list and count new number
bus.pick_up(person_1)
print(f"Bus {bus.route_number} picked up {bus.passengers[0].name}")
print(f"{bus.passenger_count()} passengers on the bus now")

# drop off passenger
bus.drop_off(person_1)
print(f"the bus dropped off {person_1.name}")
print(f"{bus.passenger_count()} passengers on the bus now")

bus.empty_bus()
print(f"all passengers please leave the bus {bus.route_number}")

bus_stop = BusStop("Craigmillar")
print(f"{bus_stop.queue_length()} passengers waiting at {bus_stop.name}")

# queue and name
bus_stop.add_to_queue(person_3)
print(f"{bus_stop.queue_length()} passenges joined the queue at {bus_stop.name}")

