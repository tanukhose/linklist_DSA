class vehicles:
    def __init__(self,type_,num_of_tyres,PriceRange,Turn_radius):
        self.type_ = type_
        self.tyres = num_of_tyres
        self.price = PriceRange
        self.rad = Turn_radius
        self.curr_speed = 0
        self.state = False
    def start(self):
        self.state = True
        return ("I am a "+self.type_+"Vehicle. I am starting")
    def stop(self):
        print("I am Stopping Now.")
    def Accelerate(self):
        if self.state==True:
            self.curr_speed+=10
        else:
            print("Start Your Vehicle First")


vehicle1 = vehicles("Car",4,500000,2)
vehicle2 = vehicles("Truck",10,5000000,5)
vehicle3 = vehicles("Bike",2,50000,1)

print(vehicle2.curr_speed)
vehicle2.start()
vehicle2.Accelerate()
print(vehicle2.curr_speed)






