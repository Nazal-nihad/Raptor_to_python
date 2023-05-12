import pickle
from fpdf import FPDF


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

    def dis_dupe(self, d_list):
        sl_no = 1
        print("sl no  Engine     Model        Car Type     Mileage   Vendor     Registration No   Owner")
        for i in d_list:
            print(
                f"{sl_no:<6}{i.engine:<14}{i.model:<14}{i.car_type:<12}{i.mileage:<9}{i.vendor:<12}{i.reg_no:<17}{i.owner}")
            sl_no += 1

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
                i.mileage = int(input("Enter Mileage : "))
                i.vendor = input("Enter vendor : ")
                i.reg_no = int(input("Enter registration number : "))
                i.owner = input("Enter owner name : ")
                return self.vehicle_list
        print("code not found")

    def sort_mileage(self):
        mileage_sorted = sorted(self.vehicle_list, key=lambda x: x.mileage)
        self.dis_dupe(mileage_sorted)

    def filtered(self):
        print("Enter the key to filter with : ")
        print("1 - Engine \n2 - model \n3 - car type \n4 - mileage \n5 - vendor \n6 - registration number \n7-owner")
        key = int(input(" : "))

        if key == 1:
            entry = input("Enter engine no : ")
            engine_sorted = [i for i in self.vehicle_list if str(
                i.engine) == str(entry)]
            self.dis_dupe(engine_sorted)

        elif key == 2:
            entry = input("Enter model no : ")
            model_sorted = [i for i in self.vehicle_list if str(
                i.model) == str(entry)]
            self.dis_dupe(model_sorted)

        elif key == 3:
            entry = input("Enter car type : ")
            car_type_sorted = [i for i in self.vehicle_list if str(
                i.car_type) == str(entry)]
            self.dis_dupe(car_type_sorted)

        elif key == 4:
            entry = input("Enter mileage : ")
            mileage_sorted = [i for i in self.vehicle_list if str(
                i.mileage) == str(entry)]
            self.dis_dupe(mileage_sorted)

        elif key == 5:
            entry = input("Enter vendor : ")
            ventor_sorted = [i for i in self.vehicle_list if str(
                i.vendor) == str(entry)]
            self.dis_dupe(ventor_sorted)

        elif key == 6:
            entry = input("Enter registration number : ")
            reg_sorted = [i for i in self.vehicle_list if str(
                i.reg_no) == str(entry)]
            self.dis_dupe(reg_sorted)

        elif key == 7:
            entry = input("Enter owner : ")
            owner_sorted = [i for i in self.vehicle_list if str(
                i.owner) == str(entry)]
            self.dis_dupe(owner_sorted)

        else:
            print("Enter a valid key ")

    def create_pickle(self):
        pickle.dump(self.vehicle_list, open(
            "vehicles_collection.pickle", "wb"))

    def load_pickle(self):
        pickle_path = input("Enter the pickle file's path")
        pickle_loaded_list = pickle.load(open(pickle_path, "rb"))
        self.dis_dupe(pickle_loaded_list)

    def report_as_pdf(self, filename):
        pdf = FPDF()
        pdf.set_title("Car Report")
        pdf.set_font("Arial", size=12)
        pdf.add_page()

        # title
        pdf.cell(0, 10, txt="Car Report", ln=True, align="C")

        # heading added
        pdf.set_font("Arial", "B", size=10)
        pdf.cell(30, 10, txt="Engine", border=1)
        pdf.cell(30, 10, txt="Model", border=1)
        pdf.cell(30, 10, txt="Car Type", border=1)
        pdf.cell(30, 10, txt="Mileage", border=1)
        pdf.cell(30, 10, txt="Vendor", border=1)
        pdf.cell(30, 10, txt="Registration No", border=1)
        pdf.cell(30, 10, txt="Owner", border=1)
        pdf.ln()

        # adding car details
        pdf.set_font("Arial", size=10)
        for vehicle in self.vehicle_list:
            pdf.cell(30, 10, txt=str(vehicle.engine), border=1)
            pdf.cell(30, 10, txt=str(vehicle.model), border=1)
            pdf.cell(30, 10, txt=str(vehicle.car_type), border=1)
            pdf.cell(30, 10, txt=str(vehicle.mileage), border=1)
            pdf.cell(30, 10, txt=str(vehicle.vendor), border=1)
            pdf.cell(30, 10, txt=str(vehicle.reg_no), border=1)
            pdf.cell(30, 10, txt=str(vehicle.owner), border=1)
            pdf.ln()

        # saved as given file name
        pdf.output(filename)

    def disp(self):
        sl_no = 1
        print("sl no  Engine     Model        Car Type     Mileage   Vendor     Registration No   Owner")
        for i in self.vehicle_list:
            print(
                f"{sl_no:<6}{i.engine:<14}{i.model:<14}{i.car_type:<12}{i.mileage:<9}{i.vendor:<12}{i.reg_no:<17}{i.owner}")
            sl_no += 1


def main():
    obj = vehicles()
    start = True
    while start:
        print("\n1 - add vehicles \n2 - delete a vehice \n3 - to modify a vehicle \n4 - sort by mileage ")
        print("5 - filter by key \n6 - save given details as pickle file \n7 - load from a pickle file ")
        print("8 - to get the details as pdf-report \n9 - to display entered detail \n10 - to exit")
        choice = int(input(" : "))

        if choice == 1:
            engine = input("Enter engine : ")
            model = input("Enter model : ")
            car_type = input("Enter car_type : ")
            mileage = input("Enter Mileage : ")
            vendor = input("Enter vendor : ")
            reg_no = input("Enter registration number : ")
            owner = input("Enter owner name : ")
            collected = car_details(
                engine, model, car_type, mileage, vendor, reg_no, owner)
            obj.add(collected)

        elif choice == 2:
            del_position = int(
                input("Enter the registration number of the car to delete : "))
            obj.delete(del_position)

        elif choice == 3:
            mod_position = int(
                input("Enter the registration number of the car to modify : "))
            obj.modify(mod_position)

        elif choice == 4:
            obj.sort_mileage()

        elif choice == 5:
            obj.filtered()

        elif choice == 6:
            obj.create_pickle()

        elif choice == 7:
            obj.load_pickle()

        elif choice == 8:
            pdf_name = input("enter the name you want to save as : ")
            pdf_name += ".pdf"
            obj.report_as_pdf(pdf_name)

        elif choice == 9:
            obj.disp()

        elif choice == 10:
            start = False
            return

        else:
            print("enter a valid number")


main()
