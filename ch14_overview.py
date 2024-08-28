from vehicle import Car, Truck
w_car = Car()
print(w_car.move_backward())
print(w_car.turn_right())

w_truck = Truck()

print(w_truck.how_many_wheels())

h = set()
print(h)
h.add(12)
print(h)
h.add(14)
h.add(18)
h.add(21)
print(h)
h.remove(14)
h.pop()
print(h)
h.pop()
print(h)
h.pop()
