from abc import ABC, abstractmethod


class demo_car(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class my_car(demo_car):

    def run(self):
        print("Stopped the car.")

    def stop(self):
        print("Run the car.")    

    def test(self)    :
       print("Testing if I can add others methods rather than abstract methods.")


car=my_car()
car.run()
car.stop()
car.test()