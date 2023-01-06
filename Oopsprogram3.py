class vehicle:
    def __init__(self,name,max_speed,mileage):
        self.name=name
        self.max_speed=max_speed
        self.mileage=mileage

#model=vehical()
#print(model.max_speed,model.mileage)

class Bus(vehicle):
    pass
school_bus=Bus("school volvo",180,12)

print("vehicle Name:",school_bus.name,"speed:",
      school_bus.max_speed,'mileage:',school_bus.mileage)

