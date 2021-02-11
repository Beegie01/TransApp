class Customer(DataReservoir):

    def __init__(self):
        self.customers['Date_Opened'].append(datetime.date(datetime.now()))
        self.customers['Time_Opened'].append(datetime.time(datetime.now()))
        #self.cust_id = None
        #self.first_name = None
        #self.last_name = None
        #self.gender = None
        #self.date_of_birth = None
        #self.birthday = None
        #self.country = None
        #self.region = None
        #self.office_addr = None


    def set_id(self):
        cust_id = str(self.customers['Date_Opened'][-1].year) + str(self.customers['Date_Opened'][-1].month)\
        + self.customers['Last_Name'][-1][:2].upper() + self.customers['Gender'][-1][0].upper() + self.customers['First_Name'][-1][:2].upper()
        self.customers['Customer_ID'].append(cust_id)
        print("Customer_ID has been set!")

    def __str__(self):
        return f"\nCUSTOMER DETAILS:\
        \nID: {self.customers['Customer_ID']}\
        \nFirst Name: {self.customers['First_Name']}\
        \nLast Name: {self.customers['Last_Name']}\
        \nGender: {self.customers['Gender']}\
        \nAge: {[(datetime.date(datetime.now()).year - yr) for yr in self.customers['Date_Opened'].year]}\
        \nBirth Day: {self.customers['Birthday']}\
        \nCountry: {self.customers['Country']}\
        \nRegion: {self.customers['Region']}\
        \nOffice Address: {self.customers['Office_Address']}\
        \nOpen Date: {self.customers['Date_Opened']}\
        \nOpen Time: {self.customers['Time_Opened']}"

    def new_customer(self):

        F = True
        while F:
            counter = 0
            val = input("First Name:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.ascii_letters:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.customers['First_Name'].append(val.capitalize())
            print("\nFirst Name Entered!")
            F = False

        L = True
        while L:
            counter = 0
            val = input("Last Name:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.ascii_letters:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.customers['Last_Name'].append(val.capitalize())
            print("\nLast Name Entered!")
            L = False

        G = True
        acc_range = ['m', 'male', 'female', 'f']
        while G:
            val = input("Gender:\t")

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
            self.customers['Gender'].append(gend.capitalize())
            print("Gender Entered!")
            G = False

        D = True
        while D:
            Yr = True
            while Yr:
                print("Please Enter Date of Birth Below\n")
                acc_range = range(1920, 2022)
                inp = input("Year:   ")

                try:
                    yr = int(inp)
                except ValueError:
                    print(f'{val} is invalid!')
                    continue

                if yr not in acc_range:
                    print(f'{val} is out of range!')
                    continue
                Yr = False

            Mon = True
            while Mon:
                acc_range = range(1,13)
                inp = input("Month:   ")

                try:
                    mon = int(inp)
                except ValueError:
                    print(f'{val} is invalid!')
                    continue

                if mon not in acc_range:
                    print(f'{val} is out of range!')
                    continue
                Mon = False

            Day = True
            while Day:
                acc_range = range(1,31)
                inp = input("Day:   ")

                try:
                    day = int(inp)
                except ValueError:
                    print(f'{val} is invalid!')
                    continue

                if day not in acc_range:
                    print(f'{val} is out of range!')
                    continue
                Day = False

            self.customers['Date_of_Birth'].append(date(yr,mon,day))
            month = self.customers['Date_of_Birth'][-1].month
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
            bday = [mon, str(self.customers['Date_of_Birth'][-1].day)]
            self.customers['Birthday'].append(' '.join(bday))
            print("Date of Birth Entered!")
            D = False

        C = True
        while C:
            counter = 0
            val = input("Country:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.ascii_letters:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.customers['Country'].append(val.capitalize())
            print("\nCountry Entered!")
            C = False

        R = True
        while R:
            counter = 0
            val = input("Region:    ")

            if val.isdigit():
                print(f'{val} is invalid!')
                continue

            for char in val:
                if char not in string.ascii_letters:
                    counter += 1

            if counter > 0:
                print(f"{val} contains wrong characters!\nPlease use only alphabets")
                continue

            self.customers['Region'].append(val.capitalize())
            print("\nRegion Entered!")
            R = False

        Addr = True
        while Addr:
            inp = input("Office Address:    ")

            if inp.isdigit():
                print(f'{val} is invalid!')
                continue

            self.customers['Office_Address'].append(inp.title())
            print("Office Address Entered!")
            Addr = False

        self.set_id()
        print("\n\nOne Customer Added!")

    def save_row_to_file(self):
            file = "C:\\Users\\welcome\\Desktop\\Transapp\\customers.txt"

            handle = open(file, 'a')

            #order_of_col: Customer_ID, First_Name, Last_Name, Gender, Date_of_Birth, Country, Region, Office_Address, Date_Opened, Time_Opened
            text = f"\n{self.cust_id}, {self.first_name}, {self.last_name}, {self.gender}, {self.date_of_birth}, {self.country}, {self.region}, {self.office_addr}, {self.date_opened}, {self.time_opened}"

            handle.write(text)

            handle.close()
