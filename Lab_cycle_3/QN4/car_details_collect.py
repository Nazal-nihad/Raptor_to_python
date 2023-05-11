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
        for i in self.vehicle_list:
            if str(i.reg_no) == str(car_reg):
                self.vehicle_list.remove(i)
                return self.vehicle_list

        print("Registration number not found ")
        return self.vehicle_list

    def modify(self, pos):
        for i in self.vehicle_list:
            if str(i.reg_no) == str(pos):
                i.engine = input("Enter engine : ")
                i.model = input("Enter model : ")
                i.car_type = input("Enter car_type : ")
                i.mileage = input("Enter Mileage : ")
                i.vendor = input("Enter vendor : ")
                i.reg_no = input("Enter registration number : ")
                i.owner = input("Enter owner name : ")
                return self.vehicle_list
        print("code not found")

    def sort_mileage(self):
        mileage_sorted = sorted(self.vehicle_list, key=lambda x: x.mileage)
        for i in mileage_sorted:
            i.display()

    def filtered(self):
        print("Enter the key to filter with : ")
        print("1 - Engine \n2 - model \n3 - car type \n4 - mileage \n5 - vendor \n6 - registration number \n7-owner")
        key = int(input(" : "))

        def dis_dupe(d_list):
            for i in d_list:
                i.display()

        if key == 1:
            entry = input("Enter engine no : ")
            engine_sorted = [i for i in self.vehicle_list if str(
                i.engine) == str(entry)]
            dis_dupe(engine_sorted)

        if key == 2:
            entry = input("Enter model no : ")
            model_sorted = [i for i in self.vehicle_list if str(
                i.model) == str(entry)]
            dis_dupe(model_sorted)

        if key == 3:
            entry = input("Enter car type : ")
            car_type_sorted = [i for i in self.vehicle_list if str(
                i.car_type) == str(entry)]
            dis_dupe(car_type_sorted)

        if key == 4:
            entry = input("Enter mileage : ")
            mileage_sorted = [i for i in self.vehicle_list if str(
                i.mileage) == str(entry)]
            dis_dupe(mileage_sorted)

        if key == 5:
            entry = input("Enter vendor : ")
            ventor_sorted = [i for i in self.vehicle_list if str(
                i.vendor) == str(entry)]
            dis_dupe(ventor_sorted)

        if key == 6:
            entry = input("Enter registration number : ")
            reg_sorted = [i for i in self.vehicle_list if str(
                i.reg_no) == str(entry)]
            dis_dupe(reg_sorted)

        if key == 7:
            entry = input("Enter owner : ")
            owner_sorted = [i for i in self.vehicle_list if str(
                i.owner) == str(entry)]
            dis_dupe(owner_sorted)

    def disp(self):
        for i in self.vehicle_list:
            #             print(i.reg_no)
            i.display()


k = vehicles()

# engine = input("Enter engine : ")
# model = input("Enter model : ")
# car_type = input("Enter car_type : ")
# mileage = input("Enter Mileage : ")
# vendor = input("Enter vendor : ")
# reg_no = input("Enter registration number : ")
# owner = input("Enter owner name : ")
# collected = car_details(engine,model, car_type, mileage, vendor, reg_no, owner)
# k.add(collected)

# engine = input("Enter engine : ")
# model = input("Enter model : ")
# car_type = input("Enter car_type : ")
# mileage = input("Enter Mileage : ")
# vendor = input("Enter vendor : ")
# reg_no = input("Enter registration number : ")
# owner = input("Enter owner name : ")
# collected = car_details(engine,model, car_type, mileage, vendor, reg_no, owner)
collected = car_details(1, 2, 3, 43, 5, 6, 7)
k.add(collected)

collected = car_details(11, 22, 33, 44, 55, 66, 77)
k.add(collected)

# k.disp()
print(" ")

# k.modify(6)
# k.disp()
# print(" ")

# k.delete(6)
k.sort_mileage()
# k.disp()
k.filtered()
