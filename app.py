from person import Person
from bus import Bus
from busstop import BusStop

# person
person_1 = Person("Steven", 34)
person_2 = Person("Laura", 21)
person_3 = Person("Wanda", 58)

# bus
bus = Bus(1, "Leith", "Tram")

# queue and name
bus_queue = BusStop("Ying")



print(f"{person_1.name}")
print(f"{bus_queue.name} is wating at {bus.destination} station")


# pick up list
bus.pick_up(person_1)

print(f"we are going to pick up {person_1}")
passenger_amount = Bus.amount_of_passengers
print({passenger_amount})
