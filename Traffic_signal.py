import threading 
import time

signal = threading.Event()

def Traffic_light():
    while True:
        print("signal Red : Stop")
        signal.clear()
        time.sleep(10)

        print("signal  Green : Go")
        signal.set()
        time.sleep(20)

        print("signal light Yellow : SlowDown")
        time.sleep(5)

def Vehicles():
    vehicle_count=0

    while True:
        print(" Vehicle waiting for the Green signal")
        signal.wait()

        print("signal is green vehicle can Go")
        while signal.is_set():
            vehicle_count +=1
            print(f"Vehicle {vehicle_count} is passing the road")
            time.sleep(2)

        print(" Signal is Red Please stop")

t1= threading.Thread(target=Traffic_light)
t2= threading.Thread(target=Vehicles)


t1.start()
t2.start()

