from Car import Car
import threading
import time

car_1 = Car("Ford","Ecosport","White",2019)

thread_x = threading.Thread(target=car_1.stop)
thread_y = threading.Thread(target=car_1.refueling)
thread_z = threading.Thread(target=car_1.turn_off )

thread_x.start()
thread_y.start()
thread_z.start()

print(threading.enumerate())



