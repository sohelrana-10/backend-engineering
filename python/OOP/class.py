class Car:

    car_count=0

    def __init__(self,model,year,color,for_sale):
        self.model=model
        self.year=year
        self.color=color
        self.for_sale=for_sale
        Car.car_count+=1


obj=Car("BMW",2026,"Black",False)
obj2=Car("BMW",2026,"Black",False)
print(obj.car_count)