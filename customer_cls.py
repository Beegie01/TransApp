import string
import datetime
from datetime import datetime, date, time


class Customer:

    count = 0

    def __init__(self):
        self.today = datetime.today()
        self.date_opened = datetime.date(self.today)
        self.time_opened = datetime.time(self.today)
        self.customer_id = None
        self.first_name = None
        self.last_name = None
        self.gender = None
        self.date_of_birth = None
        self.birthday = None
        self.country = None
        self.region = None
        self.office_addr = None
        self.last_added = []
        self.all_added = []


    def set_id(self):

        self.count += 1

        cust_id = str(self.date_opened.year) + str(self.date_opened.month)\
        + self.last_name[:2].upper() + self.gender[0].upper() + self.first_name[:2].upper()\
        + str(self.count)

        self.customer_id = cust_id
        #self.customers['Customer_ID'].append(cust_id)
        print("Customer ID has been set!")

    def __str__(self):
        return f"\nCUSTOMER DETAILS:\
        \nID: {[n[0] for n in self.all_added]}\
        \nFirst Name: {[n[1] for n in self.all_added]}\
        \nLast Name: {[n[2] for n in self.all_added]}\
        \nGender: {[n[3] for n in self.all_added]}\
        \nBirth Day: {[n[5] for n in self.all_added]}\
        \nCountry: {[n[6] for n in self.all_added]}\
        \nRegion: {[n[7] for n in self.all_added]}\
        \nOffice Address: {[n[8] for n in self.all_added]}\
        \nOpen Date: {[n[9] for n in self.all_added]}\
        \nOpen Time: {[n[10] for n in self.all_added]}"



    def fname(self):
        not_allowed = string.punctuation + string.digits
        while True:
            counter = 0
            val = input("\nFirst Name:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char in not_allowed:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.first_name = val.capitalize()
            #self.customers['First_Name'].append(val.capitalize())
            print("First Name Entered!")
            break

    def lname(self):
        not_allowed = string.punctuation + string.digits
        while True:
            counter = 0
            val = input("\nLast Name:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char in not_allowed:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.last_name = val.capitalize()
            #self.customers['Last_Name'].append(val.capitalize())
            print("Last Name Entered!")
            break

    def gend(self):
        acc_range = ['m', 'male', 'female', 'f']
        while True:
            val = input("\nGender:\t")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            elif val.lower() not in acc_range:
                print("Error: Please enter male or female!")
                continue

            if (val.lower() == 'm') or (val.lower() == 'male'):
                gend = 'male'
            elif (val.lower() == 'f') or (val.lower() == 'female'):
                gend = 'female'

            self.gender = gend.capitalize()
            #self.customers['Gender'].append(gend.capitalize())
            print("Gender Entered!")
            break

    def dob(self):
        D = True
        while D:
            Yr = True
            while Yr:
                print("\nPlease Enter Date of Birth Below\n")
                acc_range = range(1920, 2022)
                inp = input("\nYear:   ")

                try:
                    yr = int(inp)
                except ValueError:
                    print(f'{inp} is invalid!')
                    continue

                if yr not in acc_range:
                    print(f'{yr} is out of range!')
                    continue
                Yr = False

            Mon = True
            while Mon:
                acc_range = range(1,13)
                inp = input("\nMonth:   ")

                try:
                    mon = int(inp)
                except ValueError:
                    print(f'{inp} is invalid!')
                    continue

                if mon not in acc_range:
                    print(f'{mon} is out of range!')
                    continue
                Mon = False

            Day = True
            while Day:
                acc_range = range(1,31)
                inp = input("\nDay:   ")

                try:
                    day = int(inp)
                except ValueError:
                    print(f'{inp} is invalid!')
                    continue

                if day not in acc_range:
                    print(f'{day} is out of range!')
                    continue
                Day = False

            self.date_of_birth = date(yr,mon,day)

            #self.customers['Date_of_Birth'].append(date(yr,mon,day))
            month = self.date_of_birth.month
            if month == 1:
                mon = 'January'
            elif month == 2:
                mon = 'February'
            elif month == 3:
                mon = 'March'
            elif month == 4:
                mon = 'April'
            elif month == 5:
                mon = 'May'
            elif month == 6:
                mon = 'June'
            elif month == 7:
                mon = 'July'
            elif month == 8:
                mon = 'August'
            elif month == 9:
                mon = 'September'
            elif month == 10:
                mon = 'October'
            elif month == 11:
                mon = 'November'
            elif month == 12:
                mon = 'December'

            self.birthday = f'{mon}, {str(self.date_of_birth.day)}'

            #self.customers['Birthday'].append(' '.join(bday))
            print("Date of Birth Entered!")
            D = False

    def ctry(self):
        not_allowed = string.punctuation + string.digits
        while True:
            counter = 0
            val = input("\nCountry:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char in not_allowed:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.country = val.capitalize()
            #self.customers['Country'].append(val.capitalize())
            print("Country Entered!")
            break

    def regn(self):
        while True:
            counter = 0
            val = input("\nRegion:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.printable:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.region = val.capitalize()
            #self.customers['Region'].append(val.capitalize())
            print("Region Entered!")
            break

    def addr(self):
        while True:
            inp = input("\nOffice Address:    ")

            if inp.isdigit():
                print(f'{inp} is invalid!')
                continue

            self.office_addr = inp.title()
            #self.customers['Office_Address'].append(inp.title())
            print("Office Address Entered!")
            break

    def new_customer(self):

        # FIRST NAME
        self.fname()

        # LAST NAME
        self.lname()

        # GENDER
        self.gend()

        # DATE OF BIRTH
        self.dob()

        # COUNTRY
        self.ctry()

        # REGION
        self.regn()

        # OFFICE ADDRESS
        self.addr()

        self.set_id()

        add_list = [self.customer_id, self.first_name, self.last_name, self.gender, str(self.date_of_birth ),\
        self.birthday, self.country, self.region, self.office_addr, str(self.date_opened), \
        str(self.time_opened)]

        self.last_added = add_list
        ##print(self.last_added)
        self.all_added.append(self.last_added)
        #print(self.all_added)
        print("\n\nOne Customer Added!")


    def clear_last_entry(self):
        if len(self.last_added) > 0:
            self.last_added.clear()
        if len(self.all_added) > 0:
            rec = self.all_added.pop()
            print(f"{rec}\nHas Been Deleted!")
        else:
            print('\n\nNo new record to delete!')

    def commit_to_file(self):
        file = "C:\\Users\\welcome\\Desktop\\Transapp\\customers.txt"

        handle = open(file, 'a')

        #DELIM = ', '
        #order_of_col: Customer_ID, First_Name, Last_Name, Gender, Date_of_Birth, Birthday, Country, Region, Office_Address, Date_Opened, Time_Opened
        text = f"\n{[new for new in self.all_added]}"

        handle.write(text)

        handle.close()

        print('\n\nCustomer Details Saved!')
