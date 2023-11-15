class Vehicle:

    def __init__(self):
        self.num_of_wheels = 0
    
    def move_backward(self):
        pass

    def move_forward(self):
        pass

    def has_motor(self):
        pass

    def has_engine(self):
        pass

    def turn_left(self):
        pass

    def turn_right(self):
        pass



class Car(Vehicle):
    def __init__(self):
        self.num_of_wheels = 4
        self.motor = True

    def how_many_wheels(self):
        return self.num_of_wheels
      
    def has_motor(self):
        return self.motor

class Truck(Vehicle):
    def __init__(self):
        self.num_of_wheels = 6
        self.motor = True

    def how_many_wheels(self):
        return self.num_of_wheels

    def has_motor(self):
        return self.motor

class Motorcycle(Vehicle):
    def __init__(self):
        self.num_of_wheels = 2
        self.motor = True

    def how_many_wheels(self):
        return self.num_of_wheels

    def has_motor(self):
        return self.motor

if __name__ == '__main__' :
    c = Car()
    t = Truck()
    m = Motorcycle()

    print(c.how_many_wheels())
    print(t.how_many_wheels())
    print(m.how_many_wheels())
    print(c.has_motor())
    print(t.has_motor())
    print(m.has_motor())
    


