import time
class Car:
    def __init__(self,make,model,color,year):
          self.make = make
          self.model = model 
          self.color = color
          self.year = year

    def drive(self):
        print(self.make + " is driving")

    def turn_off(self):
        time.sleep(2)
        print(self.make + " is off")

    def refueling(self):
        time.sleep(4)
        print(self.make + " is refueling")

    def stop(self):
        time.sleep(5)
        print(self.make + " is stopped")
    