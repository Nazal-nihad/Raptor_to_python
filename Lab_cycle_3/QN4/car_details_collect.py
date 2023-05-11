class car_details:
    def __init__(self, engine=0, model=0, car_type=0, mileage=0, vendor=0, reg_no=0, owner=0):
        self.engine = engine
        self.model = model
        self.car_type = car_type
        self.mileage = mileage
        self.vendor = vendor
        self.reg_no = reg_no
        self.owner = owner

    def display(self):
        print(f"{self.engine}\t{self.model}\t{self.car_type}\t{self.mileage}\t{self.vendor}\t{self.reg_no}\t{self.owner}")


class vehicles(car_details):
    def __init__(self):
        self.vehicle_list = list()

    def add(self, vehicle):
        self.vehicle_list.append(vehicle)

    def delete(self, car_reg):
        flag = 0
        for i in self.vehicle_list:
            if i.reg_no == car_reg:
                flag = i
            if flag != 0:
                self.vehicle_list.remove(flag)
            else:
                print("Numbers don't match")

    def modify(self, pos):
        for i in self.vehicle_list:
            if i.reg_no == pos:
                model = input("Enter model : ")
                car_type = input("Enter car_type : ")
                mileage = input("Enter Mileage : ")
                vendor = input("Enter vendor : ")
                reg_no = input("Enter registration number : ")
                owner = input("Enter owner name : ")

                collected = (model, car_type, mileage, vendor, reg_no, owner)
                self.vehicle_list[i] = collected

    def disp(self):
        for i in self.vehicle_list:
            print(i.reg_no)
            i.display()


k = vehicles()

model = input("Enter model : ")
car_type = input("Enter car_type : ")
mileage = input("Enter Mileage : ")
vendor = input("Enter vendor : ")
reg_no = input("Enter registration number : ")
owner = input("Enter owner name : ")
collected = car_details(model, car_type, mileage, vendor, reg_no, owner)
k.add(collected)

model = input("Enter model : ")
car_type = input("Enter car_type : ")
mileage = input("Enter Mileage : ")
vendor = input("Enter vendor : ")
reg_no = input("Enter registration number : ")
owner = input("Enter owner name : ")
collected = car_details(model, car_type, mileage, vendor, reg_no, owner)
k.add(collected)

k.disp()
k.delete(5)
k.disp()
