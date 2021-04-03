import tkinter as tk, datetime, random, os
from tkinter import messagebox
from inventory_cls import Inventory
from customer_cls import Customer
from sales_cls import Sales


dir_path = 'C:\\Users\\welcome\\Desktop\\MyFuncs'

if dir_path not in os.sys.path:
    os.sys.path.append(dir_path)

from mydict_funcs import del_item

class TransApp:

    def __init__(self, master): #, inventory_obj, customer_obj, sales_obj):
        self.master = master
        # create an object of inventory
        self.inv_obj = Inventory()
        # create an object of customer
        self.cust_obj = Customer()
        # create an object of sales
        self.sales_obj = Sales()

        # menu bar section
        self.menu_bar = tk.Menu(self.master)
        self.master.config(menu=self.menu_bar)
        main_menu = tk.Menu(self.menu_bar, tearoff=0)
        main_menu.add_command(label="HOME", command=lambda: self.menupage())
        main_menu.add_command(label="EXIT", command=lambda: self.master.destroy())
        self.menu_bar.add_cascade(menu=main_menu, label='MENU')

        # status bar frame
        self.status_bar_frame = None

        # frame for front page containing one row and one column
        self.frame1 = None

        # frame for menu page containing four rows and one column
        self.frame2 = None

        # frame for inventory page containing three rows and one column
        self.frameinv = None

        # frame for input of new inventory
        self.new_prod_frame = None

        # frame for submission status
        self.submit_frame = None

        self.display_frame = None

        self.edit_prod_frame = None

    def setup_frames(self):
        # status bar frame
        self.status_bar_frame = tk.Frame(master=self.master, bg='gold')
        self.status_bar_frame.rowconfigure(0, weight=1)
        self.status_bar_frame.columnconfigure([0, 1, 2, 3, 4], weight=1)
        self.status_bar_frame.grid(row=0, column=0, columnspan=5, sticky='we')

        # frame for front page containing one row and one column
        self.frame1 = tk.Frame(master=self.master, bg='GOLD')
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.columnconfigure(0, weight=1)

        # frame for menu page containing four rows and one column
        self.frame2 = tk.LabelFrame(master=self.master, text='HOME', fg='black', font=('arial black', 12))
        self.frame2.rowconfigure([0, 1, 2, 3], weight=1)
        self.frame2.columnconfigure(0, weight=1)

        # frame for inventory page containing three rows and one column
        self.frameinv = tk.LabelFrame(master=self.master, text='INVENTORY', font=('arial black', 12), bg='purple',
                                      fg='white')
        self.frameinv.rowconfigure([0, 1, 2, 3], weight=1)
        self.frameinv.columnconfigure(0, weight=1)

        # frame for input of new inventory
        self.new_prod_frame = tk.LabelFrame(self.master, text='NEW PRODUCT', fg='white', font=('arial black', 12),
                                            bg='purple')
        self.new_prod_frame.rowconfigure(list(range(4)), weight=1)
        self.new_prod_frame.columnconfigure(list(range(3)), weight=1)

        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
                                          font=('arial black', 12), bg='purple')
        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(0, weight=1)

        self.edit_prod_frame = tk.LabelFrame(self.master, font=('arial black', 12), bg='purple')
        self.edit_prod_frame.rowconfigure(0, weight=1)
        self.edit_prod_frame.columnconfigure(0, weight=1)

    def make_frame(self, page_title=None, background_color='purple', foreground_color='white'):
        # specify the frame text, fg, bg
        return tk.LabelFrame(self.master, text=page_title, bg=background_color, fg=foreground_color, font=('arial black', 12))

    def setup_status_bar(self):
        # status bar
        self.status_date = tk.Label(master=self.status_bar_frame, font=('arial black', 12), fg='black', bg='gold',
                                    text=f"{datetime.datetime.date(datetime.datetime.today())}")
        self.status_date.grid(row=0, column=4, sticky='ew')
        self.status_appname = tk.Label(master=self.status_bar_frame, font=('arial black', 12), fg='black', bg='gold',
                                       text=f"TransApp March 2021")
        self.status_appname.grid(row=0, column=3, sticky='nsew')

    def frontpage(self):
        # place label on frame
        frontlabel = tk.Label(master=self.frame1, text='\nTRANSAPP\n\nBY\n\nBEEGIE\n\nMARCH, 2021', fg='black', bg='gold', font=('Arial Black', 20))
        frontlabel.grid(row=0, sticky='nsew')
        menuButton = tk.Button(self.frame1, text=" CLICK HERE TO START ", fg='white', bg='green',
                                  font=('arial black', 14), command=self.menupage)
        menuButton.grid(row=1, sticky='sew')

        # place label frame on app frame starting at row 1, column 0
        self.frame1.grid(row=0, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def menupage(self):
        # frame for menu page containing four rows and one column
        self.frame2 = tk.LabelFrame(master=self.master, text='HOME', fg='black', font=('arial black', 12))
        self.frame2.rowconfigure([0, 1, 2, 3], weight=1)
        self.frame2.columnconfigure(0, weight=1)

        # menu sections
        self.inventoryb = tk.Button(self.frame2, text="INVENTORY", fg='white', bg='purple',
                                    font=('arial black', 14), command=lambda: self.invenpage())
        self.customerb = tk.Button(self.frame2, text="CUSTOMERS", fg='white', bg='blue',
                                   font=('arial black', 14), command=lambda: self.custpage())
        self.salesb = tk.Button(self.frame2, text="SALES", fg='white', bg='brown',
                                font=('arial black', 14), )
        self.accountb = tk.Button(self.frame2, text="ACCOUNTS", fg='white', bg='green',
                                  font=('arial black', 14), )
        # menu sections
        self.inventoryb.grid(row=0, padx=40, sticky='nsew')
        self.customerb.grid(row=1, padx=30, sticky='nsew')
        self.salesb.grid(row=2, padx=20, sticky='nsew')
        self.accountb.grid(row=3, padx=10, sticky='nsew')

        # display frame of menupage
        # clear frame space
        if self.frame1 is not None:
            self.frame1.grid_forget()
        if self.frameinv is not None:
            self.frameinv.grid_forget()
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()

        self.frame2.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def invenpage(self):
        # frame for inventory page containing three rows and one column
        self.frameinv = tk.LabelFrame(master=self.master, text='INVENTORY', font=('arial black', 12), bg='purple',
                                      fg='white')
        self.frameinv.rowconfigure([0, 1, 2, 3], weight=1)
        self.frameinv.columnconfigure(0, weight=1)

        self.create = tk.Button(self.frameinv, text='ADD NEW PRODUCT TO INVENTORY', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_prod)
        self.edit = tk.Button(self.frameinv, text='UPDATE INVENTORY', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_prod)
        self.dele = tk.Button(self.frameinv, text='DELETE RECORD FROM INVENTORY', bg='white', fg='red',
                              font=('arial black', 14), command=self.delete_prod)
        self.view = tk.Button(self.frameinv, text='VIEW INVENTORY RECORDS', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_inv())

        # display inventory options
        self.view.grid(row=0, padx=40, pady=10, sticky='nsew')
        self.create.grid(row=1, padx=60, pady=10, sticky='nsew')
        self.edit.grid(row=2, padx=80, pady=10, sticky='nsew')
        self.dele.grid(row=3, padx=100, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()
        if self.frame2 is not None:
            self.frame2.grid_forget()

        self.frameinv.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def custpage(self):
        # frame for customer page containing three rows and one column
        self.frameinv = tk.LabelFrame(master=self.master, text='CUSTOMER', font=('arial black', 12), bg='blue',
                                      fg='white')
        self.frameinv.rowconfigure([0, 1, 2, 3], weight=1)
        self.frameinv.columnconfigure(0, weight=1)

        self.create = tk.Button(self.frameinv, text='ADD NEW CUSTOMER', bg='white', fg='blue',
                                font=('arial black', 14), command=self.new_cust)
        self.edit = tk.Button(self.frameinv, text='UPDATE CUSTOMER RECORD', bg='white', fg='orange',
                              font=('arial black', 14), command=self.edit_cust)
        self.dele = tk.Button(self.frameinv, text='DELETE CUSTOMER RECORD', bg='white', fg='red',
                              font=('arial black', 14), command=self.delete_cust)
        self.view = tk.Button(self.frameinv, text='VIEW CUSTOMER RECORDS', bg='white', fg='green',
                              font=('arial black', 14), command=lambda: self.display_cust())

        # display inventory options
        self.view.grid(row=0, padx=40, pady=10, sticky='nsew')
        self.create.grid(row=1, padx=60, pady=10, sticky='nsew')
        self.edit.grid(row=2, padx=80, pady=10, sticky='nsew')
        self.dele.grid(row=3, padx=100, pady=10, sticky='nsew')

        # display inventory page's frame
        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()
        if self.frame2 is not None:
            self.frame2.grid_forget()

        self.frameinv.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def new_cust(self):
        bg, fg = 'blue', 'white'

        # frame for input of new inventory
        self.new_prod_frame = tk.LabelFrame(self.master, text='NEW CUSTOMER REGISTRATION', fg=fg, font=('arial black', 12),
                                            bg=bg)
        self.new_prod_frame.rowconfigure(list(range(9)), weight=1)
        self.new_prod_frame.columnconfigure(list(range(5)), weight=1)

        # place new customer form
        # customer Name
        tk.Label(self.new_prod_frame, text='Customer', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nsew')
        # first name
        tk.Label(self.new_prod_frame, text='First Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=1, stick='nw')
        self.fnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
        self.fnameEntry.grid(row=0, column=1, padx=2, pady=30, stick='sw')
        # middle name
        tk.Label(self.new_prod_frame, text='Middle Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='nw')
        self.midnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
        self.midnameEntry.grid(row=0, column=2, padx=2, pady=30, stick='sw')
        # last name
        tk.Label(self.new_prod_frame, text='Last Name', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=0, column=3, stick='nw')
        self.lnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
        self.lnameEntry.grid(row=0, column=3, padx=2, pady=30, stick='sw')

        # customer Gender
        tk.Label(self.new_prod_frame, text='Gender:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=1, column=0, padx=10, stick='nsew')
        gend = tk.StringVar(value='None')
        # gend.set("")
        maleRadio = tk.Radiobutton(self.new_prod_frame, text='Male', val='Male', variable=gend,
                                   bg=bg, fg=fg, command=lambda: self.sel_gender(gend.get()), state='normal')
        maleRadio.grid(row=1, column=1, padx=2, sticky='w')
        femaleRadio = tk.Radiobutton(self.new_prod_frame, text='Female', val='Female', variable=gend,
                                     bg=bg, fg=fg, command=lambda: self.sel_gender(gend.get()), state='normal')
        femaleRadio.grid(row=1, column=2, padx=2, sticky='w')

        # customer date of birth
        tk.Label(self.new_prod_frame, text='Date of Birth:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nsew')
        # day
        tk.Label(self.new_prod_frame, text='Day', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=1, padx=5, stick='nw')
        self.regdayEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regdayEntry.insert(0, str(datetime.date.today().day))
        self.regdayEntry.grid(row=2, column=1, padx=5, pady=30, stick='sw')
        # month
        tk.Label(self.new_prod_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=2, padx=5, stick='nw')
        self.regmonthEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regmonthEntry.insert(0, str(datetime.date.today().month))
        self.regmonthEntry.grid(row=2, column=2, padx=5, pady=30, stick='sw')
        # year
        tk.Label(self.new_prod_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=2, column=3, stick='nw')
        self.regyrEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regyrEntry.insert(0, str(datetime.date.today().year))
        self.regyrEntry.grid(row=2, column=3, pady=30, stick='sw')

        # nationality
        tk.Label(self.new_prod_frame, text='Nationality:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=0, padx=10, stick='nsew')
        tk.Label(self.new_prod_frame, text='Country', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=1, padx=10, stick='nw')
        self.natEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.natEntry.grid(row=3, column=1, padx=5, pady=30, stick='sw')

        # state of origin
        tk.Label(self.new_prod_frame, text='State of Origin:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=3, column=2, padx=0, pady=0, stick='nw')
        self.stateEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.stateEntry.grid(row=3, column=2, padx=5, pady=30, stick='sw')

        # Office address
        tk.Label(self.new_prod_frame, text='Office Address:', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=4, column=0, padx=5, stick='nsew')
        self.off_addrText = tk.Text(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10, height=3)
        self.off_addrText.grid(row=4, column=1, padx=5, pady=30, sticky='ew')

        # date of registration
        tk.Label(self.new_prod_frame, text='As of Date:', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=0, padx=5, pady=0, sticky='nsew')
        # day
        tk.Label(self.new_prod_frame, text='Day', font=('calibri', 16),
                 bg=bg, fg=fg, height=1).grid(row=5, column=1, padx=5, sticky='nw')
        self.regdayEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regdayEntry.insert(0, str(datetime.date.today().day))
        self.regdayEntry.grid(row=5, column=1, padx=5, pady=30, sticky='sw')
        # month
        tk.Label(self.new_prod_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=2, padx=5, sticky='nw')
        self.regmonthEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regmonthEntry.insert(0, str(datetime.date.today().month))
        self.regmonthEntry.grid(row=5, column=2, padx=5, pady=30, sticky='sw')
        # year
        tk.Label(self.new_prod_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
                 height=1).grid(row=5, column=3, sticky='nw')
        self.regyrEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.regyrEntry.insert(0, str(datetime.date.today().year))
        self.regyrEntry.grid(row=5, column=3, pady=30, sticky='sw')

        submitButton = tk.Button(self.new_prod_frame, text='Submit', font=("Calibri", 14, 'bold'),
                                 fg='white', bg='green', width=10, height=2, command=self.submitcust)
        submitButton.grid(row=7, column=2, padx=10, sticky='se')

        custpageb = tk.Button(self.new_prod_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
                             fg='blue', bg='white', height=2, width=15, command=self.custpage)
        custpageb.grid(row=7, column=0, padx=15, stick='se')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.frameinv is not None:
            self.frameinv.grid_forget()

        self.new_prod_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')

    def sel_gender(self, selected_gender):
        self.cust_obj.gender = selected_gender
        print(self.cust_obj.gender)

    def submitcust(self):
        pass

    def edit_cust(self):
        pass

    def delete_cust(self):
        pass

    def display_cust(self):
        pass


    def new_prod(self):
        # frame for input of new inventory
        self.new_prod_frame = tk.LabelFrame(self.master, text='NEW PRODUCT', fg='white', font=('arial black', 12),
                                            bg='purple')
        self.new_prod_frame.rowconfigure(list(range(4)), weight=1)
        self.new_prod_frame.columnconfigure(list(range(3)), weight=1)

        # place new inventory form
        tk.Label(self.new_prod_frame, text='Product Name:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=0, column=0, padx=5, pady=50, sticky='ew')
        self.pnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
        self.pnameEntry.grid(row=0, column=1, padx=5, pady=50, sticky='ew')

        # stock entries
        tk.Label(self.new_prod_frame, text='New Stock:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=0, padx=5, pady=50, sticky='sew')
        tk.Label(self.new_prod_frame, text='Quantity (in figures)', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=1, padx=5, sticky='nw')
        self.qtyEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.qtyEntry.grid(row=1, column=1, padx=5, pady=50, sticky='sw')

        tk.Label(self.new_prod_frame, text='Unit of Measurement', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=1, column=2, padx=0, sticky='nw')
        self.unitEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.unitEntry.grid(row=1, column=2, padx=5, pady=50, sticky='sw')

        # date entries
        tk.Label(self.new_prod_frame, text='As of Date:', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=0, padx=5, pady=50, sticky='sew')
        # day
        tk.Label(self.new_prod_frame, text='Day', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=1, padx=5, sticky='nw')
        self.dayEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.dayEntry.insert(0, str(datetime.date.today().day))
        self.dayEntry.grid(row=2, column=1, padx=5, pady=50, sticky='sw')
        # month
        tk.Label(self.new_prod_frame, text='Month', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, padx=5, sticky='nw')
        self.monthEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.monthEntry.insert(0, str(datetime.date.today().month))
        self.monthEntry.grid(row=2, column=2, padx=5, pady=50, sticky='sw')
        # year
        tk.Label(self.new_prod_frame, text='Year', font=('calibri', 16),
                 bg='purple', fg='white', height=1).grid(row=2, column=2, sticky='n')
        self.yrEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
        self.yrEntry.insert(0, str(datetime.date.today().year))
        self.yrEntry.grid(row=2, column=2, pady=50, sticky='s')

        # submit and inventory page buttons
        submitButton = tk.Button(self.new_prod_frame, text='Submit', font=("Calibri", 14, 'bold'),
                                 fg='white', bg='green', width=3, height=2, command=self.submitinv)
        submitButton.grid(row=3, column=2, padx=350, sticky='ew')
        invpageb = tk.Button(self.new_prod_frame, text='Inventory Page', font=("Calibri", 14, 'bold'),
                             fg='purple', bg='white', height=2, width=15, command=self.invenpage)
        invpageb.grid(row=3, column=1, padx=5, stick='w')

        # display inventory page's frame
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.frameinv is not None:
            self.frameinv.grid_forget()

        self.new_prod_frame.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')

    def ID_gen(self):
        # randomly generates a five-character output
        num = random.randint(100, 999)
        al1 = random.choice('ABCDFJKLMNQWERTPOIUY')
        al2 = random.choice('abcdfjklmnqwertpoiuy')
        return f"{num}{al1}{al2}"

    def submitinv(self):
        # frame for submission status
        self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
                                          font=('arial black', 12), bg='purple')
        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)

        # check for data integrity
        entries = [self.pnameEntry.get(), self.qtyEntry.get(), self.unitEntry.get(), self.yrEntry.get(),
                            self.monthEntry.get(), self.dayEntry.get()]
        cond = [None, '', ' ']
        # any of the field is empty
        if [True for entry in entries if entry in cond]:
            return messagebox.showerror(title='Blank Field', message='Blank field detected!')
        # product name and units cannot be numbers
        if [entry for entry in [self.pnameEntry.get(), self.unitEntry.get()] if entry.isdigit()]:
            return messagebox.showerror(title='Invalid Data Type', message='Product name,\nUnit of measurement\n\tcannot be a number!')
        # qty, yr, month, day must be numbers
        if [entry for entry in [self.qtyEntry.get(), self.yrEntry.get(), self.monthEntry.get(), self.dayEntry.get()] if not(entry.isdigit())]:
            return messagebox.showerror(title='Invalid Data Type', message='Quantity,\nDay,\nMonth,\nYear\n\tmust be in figures!')

        # assign user input from entry to each inventory class attribute
        self.inv_obj.prod_id = f"{''.join([word[0] for word in self.pnameEntry.get().title().split()])}{self.ID_gen()}"
        self.inv_obj.prod_name = self.pnameEntry.get().title()
        self.inv_obj.qty = self.qtyEntry.get()
        self.inv_obj.unit = self.unitEntry.get().title()
        self.inv_obj.entry_date = f"{self.yrEntry.get()}-{self.monthEntry.get()}-{self.dayEntry.get()}"

        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                                       text=f"ID:\n{self.inv_obj.prod_id}").grid(row=0, column=0, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"PRODUCT:\n{self.inv_obj.prod_name}").grid(row=0, column=1, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"QTY:\n{self.inv_obj.qty} {self.inv_obj.unit}").grid(row=0, column=2, sticky='ew')
        tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='purple', fg='white',
                 text=f"DATE:\n{self.inv_obj.entry_date}").grid(row=0, column=3, sticky='ew')

        saveb = tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'),
                          bg='green', fg='white', height=5, width=15, command=self.saveinv)
        saveb.grid(row=1, column=0, padx=5, stick='ew')
        cancelb = tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'),
                            bg='red', fg='white', height=5, width=15, command=self.new_prod)
        cancelb.grid(row=1, column=3, padx=5, stick='ew')

        if self.display_frame is not None:
            self.display_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        self.submit_frame.grid(row=1, sticky='nsew')

    def saveinv(self):
        with open(self.inv_obj.inv_data, 'a',
                  encoding='utf8') as hand:
            hand.writelines(f"{self.inv_obj.__dict__}\n")

        self.submit_frame = self.make_frame()

        saved = tk.Label(self.submit_frame, text='NEW INVENTORY HAS BEEN ADDED!', font=("arial", 14, 'bold'),
                         bg='purple', fg='white')
        saved.grid(row=0, column=0, columnspan=4, sticky='nsew')

        addb = tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'),
                         bg='blue', fg='white', height=5, width=15, command=self.new_prod)
        addb.grid(row=1, column=0, padx=5, stick='ew')

        invpageb = tk.Button(self.submit_frame, text='Inventory Page', font=("Calibri", 14, 'bold'),
                             fg='purple', bg='white', height=5, width=15, command=self.invenpage)
        invpageb.grid(row=1, column=3, padx=5, stick='ew')

        self.submit_frame.rowconfigure([0, 1], weight=1)
        self.submit_frame.columnconfigure(list(range(4)), weight=1)
        self.submit_frame.grid(row=1, sticky='nsew')

    def read_inv(self):
        with open(self.inv_obj.inv_data, 'r', encoding='utf8') as hand:
            # inventory attributes is a list of record strings
            inv_attr = hand.readlines()
            # print(inv_attr)
        return inv_attr

    def display_inv(self):
        global inven, lines

        inven = []
        lines = {}

        # setup display frame
        self.display_frame = self.make_frame(page_title='INVENTORY RECORDS VIEW')

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines['Row_'+str(ind)] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        # display headings for inventory records
        tk.Label(self.display_frame, text=f"PRODUCT ID", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='e')
        tk.Label(self.display_frame, text=f"PRODUCT NAME", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew')
        tk.Label(self.display_frame, text=f"STOCK (in units)", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew')
        tk.Label(self.display_frame, text=f"DATE OF ENTRY", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]

            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_id}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind+1, column=0, sticky='e')
            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind+1, column=1, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind+1, column=2, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind+1, column=3, sticky='nsew')

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=len(inven)+2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(inven) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven)+2, column=0, columnspan=4, sticky='nsew')

    def edit_prod(self):
        global edit_prodid_entry, inven, lines

        # setup display frame
        self.display_frame = self.make_frame(page_title='EDIT INVENTORY RECORDS')

        inven = []
        lines = {}

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()
        print(len(inven_rec))

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines[ind] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        # display headings for inventory records
        tk.Label(self.display_frame, text=f"PRODUCT ID", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='e')
        tk.Label(self.display_frame, text=f"PRODUCT NAME", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew')
        tk.Label(self.display_frame, text=f"STOCK (in units)", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew')
        tk.Label(self.display_frame, text=f"DATE OF ENTRY", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]

            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_id}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=0, sticky='e')
            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=1, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=2, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=3, sticky='nsew')

        tk.Label(self.display_frame, text='ENTER PRODUCT ID:', font=("Calibri", 10, 'bold'), bg='purple',
                 fg='white').grid(row=len(inven) + 2, column=0, padx=2, sticky='e')

        edit_prodid_entry = tk.Entry(self.display_frame, font=("Calibri", 10, 'bold'))
        edit_prodid_entry.grid(row=len(inven) + 2, column=1, padx=2, sticky='w')

        # to edit the given row number (at row entry - 1)
        tk.Button(self.display_frame, text='Edit', font=("Calibri", 12, 'bold'),
                             bg='orange', fg='white', height=1, width=10, command=self.editing).grid(row=len(inven) + 2, column=1,
                                                                                           sticky='e')
        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=len(inven) + 2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(inven)+2)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven)+2, column=0, columnspan=4, sticky='nsew')

    def editing(self):
        global edit_prodid_entry, inven, lines, edit_row_num

        self.display_frame = self.make_frame(page_title='UPDATING INVENTORY RECORD')

        prod_ids = []

        for rec in inven:
            prod_ids.extend([v.lower() for k,v in rec.items() if k.lower() == 'prod_id'])

        inp = edit_prodid_entry.get()

        if inp.lower() not in prod_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        # get the row index of the selected product id
        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'prod_id' and v.lower() == inp.lower():
                    edit_row_num = row
                    # print(f"Found at {edit_row_num}")

        # assign the selected record to the inventory object
        for row, rec in lines.items():
            if row == edit_row_num:
                self.inv_obj.__dict__ = rec
        print(self.inv_obj.__dict__)
        tk.Label(self.display_frame, text="SELECTED DATA", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, columnspan=3, sticky='ew', padx=50)

        tk.Label(self.display_frame, text=f"ID:\n\n{self.inv_obj.prod_id}: ", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=0, sticky='ew', padx=25)
        tk.Label(self.display_frame, text=f"PRODUCT NAME:\n\n{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, sticky='ew', padx=25)
        tk.Label(self.display_frame, text=f"STOCK:\n\n{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=2, sticky='ew', padx=25)
        tk.Label(self.display_frame, text=f"DATE:\n\n{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=3, sticky='ew', padx=25)

        tk.Label(self.display_frame, text=f"ENTER NEW DATA BELOW", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=2, columnspan=3, sticky='ew', padx=50)

        # product labels and entries
        tk.Label(self.display_frame, text=f"PRODUCT:", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=0, sticky='ew', padx=50, pady=15)

        # product name label and entry
        tk.Label(self.display_frame, text=f"NAME", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=1, sticky='nw', padx=25, pady=15)
        self.pname_entry = tk.Entry(self.display_frame)
        self.pname_entry.grid(row=3, column=1, sticky='w', padx=25, pady=5)

        # product quantity label and entry
        tk.Label(self.display_frame, text=f"QUANTITY", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=2, sticky='nw', padx=25, pady=15)
        self.pqty_entry = tk.Entry(self.display_frame)
        self.pqty_entry.grid(row=3, column=2, sticky='w', padx=25, pady=5)

        # unit of measurement label and entry
        tk.Label(self.display_frame, text=f"Unit of Measurement", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=3, column=3, sticky='nw', padx=25, pady=15)
        self.punit_entry = tk.Entry(self.display_frame)
        self.punit_entry.grid(row=3, column=3, sticky='w', padx=25, pady=5)

        # date labels and entries section
        tk.Label(self.display_frame, text=f"DATE", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=0, sticky='ew', padx=25, pady=15)
        # Year label and entry
        tk.Label(self.display_frame, text=f"YEAR", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=1, sticky='nw', padx=25, pady=15)
        self.yr_entry = tk.Entry(self.display_frame)
        self.yr_entry.grid(row=4, column=1, sticky='w', padx=25, pady=5)
        # Month label and entry
        tk.Label(self.display_frame, text=f"MONTH", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=2, sticky='nw', padx=25, pady=15)
        self.mon_entry = tk.Entry(self.display_frame)
        self.mon_entry.grid(row=4, column=2, sticky='w', padx=25, pady=5)
        # Day label and entry
        tk.Label(self.display_frame, text=f"DAY", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=4, column=3, sticky='nw', padx=25, pady=15)
        self.day_entry = tk.Entry(self.display_frame)
        self.day_entry.grid(row=4, column=3, sticky='w', padx=25, pady=5)

        # update and inventory page buttons
        updateb = tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'),
                            bg='orange', fg='white', height=1, width=15, command=self.update)
        updateb.grid(row=len(inven) + 2, column=1, padx=5, pady=5, stick='sw')

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=len(inven) + 2, column=3, padx=5, pady=5, stick='sw')

        # clear the frames before and after this page
        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        # display an adjustible frame containing the selected info
        self.display_frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

    def update(self):
        global lines, edit_row_num
        # raise error alarm if any of the field is blank
        edited_entries = [self.pname_entry.get(), self.pqty_entry.get(), self.punit_entry.get(), self.yr_entry.get(), self.mon_entry.get(), self.day_entry.get()]
        blanks = ['', ' ']
        # when a field is blank
        if [True for entry in edited_entries if entry in blanks]:
            return messagebox.showerror(message="BLANK FIELD(S) DETECTED!")
        # when product name or unit of measurement is given in figures
        if [True for entry in [self.pname_entry.get(), self.punit_entry.get()] if entry.isdigit()]:
            return messagebox.showerror(message="PRODUCT NAME\nUNIT OF MEASUREMENT\n\nCannot contain only numbers")
        # when qty, date fields is/are not given in figures
        if [True for entry in [self.pqty_entry.get(),self.yr_entry.get(), self.mon_entry.get(), self.day_entry.get()] if not(entry.isdigit())]:
            return messagebox.showerror(message="QUANTITY\nDAY\nMONTH\nYEAR\nMust contain numbers only")

        if not(messagebox.askyesno(title='CONFIRM UPDATE', message='Do You Want to Continue?')):
            return messagebox.showinfo(message='NO CHANGES MADE TO INVENTORY')

        # when confirmation is given by user
        self.display_frame = self.make_frame()

        # reassign the newly entered values to the inventory object's name, qty, unit and date
        self.inv_obj.prod_name = self.pname_entry.get().title()
        self.inv_obj.qty, self.inv_obj.unit = self.pqty_entry.get(), self.punit_entry.get().title()
        self.inv_obj.entry_date = f"{self.yr_entry.get()}-{self.mon_entry.get()}-{self.day_entry.get()}"

        # update the retrieved data from file with the changes made
        lines[edit_row_num] = self.inv_obj.__dict__

        # save updated version to file
        # print([rec for row, rec in lines.items()])
        # print(Inventory.inv_data)
        with open(Inventory.inv_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                hand.writelines(f"{rec}\n")

        tk.Label(self.display_frame, text=f"PRODUCT\n{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='nsew', padx=25, pady=15)
        tk.Label(self.display_frame, text=f"ID\n{self.inv_obj.prod_id}: ", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"STOCK:\n{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"DATE:\n{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text="HAS BEEN UPDATED!!", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, columnspan=2, sticky='NSEW', padx=25)

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

    def delete_prod(self):
        global lines, inven, del_row, del_prodid_entry

        self.display_frame = self.make_frame("DELETE RECORD")

        inven = []
        lines = {}

        # retrieve inventory data from file
        # inven is a list of strings containing inventory records
        inven_rec = self.read_inv()
        print(len(inven_rec))

        for ind in range(len(inven_rec)):
            # labelled format of saved inventory record
            lines[ind] = eval(inven_rec[ind])
            # inven is a list of saved inventory instances
            inven.append(eval(inven_rec[ind]))

        # display headings for inventory records
        tk.Label(self.display_frame, text=f"PRODUCT ID", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='e')
        tk.Label(self.display_frame, text=f"PRODUCT NAME", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew')
        tk.Label(self.display_frame, text=f"STOCK (in units)", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew')
        tk.Label(self.display_frame, text=f"DATE OF ENTRY", font=("Calibri", 14, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew')

        for ind in range(len(inven)):
            # assign user input from stored inventory records to each inventory class attribute
            self.inv_obj.__dict__ = inven[ind]

            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_id}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=0, sticky='e')
            tk.Label(self.display_frame, text=f"{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=1, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=2, sticky='nsew')
            tk.Label(self.display_frame, text=f"{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                     bg='purple', fg='white').grid(row=ind + 1, column=3, sticky='nsew')

        tk.Label(self.display_frame, text='ENTER PRODUCT ID:', font=("Calibri", 10, 'bold'), bg='purple',
                 fg='white').grid(row=len(inven) + 2, column=0, padx=2, sticky='e')

        del_prodid_entry = tk.Entry(self.display_frame, font=("Calibri", 10, 'bold'))
        del_prodid_entry.grid(row=len(inven) + 2, column=1, padx=2, sticky='w')
        # to edit the given row number (at row entry - 1)
        tk.Button(self.display_frame, text='Delete', font=("Calibri", 12, 'bold'),
                  bg='red', fg='white', height=1, width=10, command=self.erase_inv).grid(row=len(inven) + 2,
                                                                                         column=1,
                                                                                         sticky='e')
        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=len(inven) + 2, column=3, padx=5, pady=5, stick='se')

        if self.submit_frame is not None:
            self.submit_frame.grid_forget()
        if self.edit_prod_frame is not None:
            self.edit_prod_frame.grid_forget()
        if self.new_prod_frame is not None:
            self.new_prod_frame.grid_forget()

        self.display_frame.rowconfigure(list(range(len(inven) + 2)), weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

    def erase_inv(self):
        global lines, prod_ids, del_row, del_prodid_entry
        # raise error alarm if any of the field is blank

        self.display_frame = self.make_frame(page_title='RECORD DELETED')

        prod_ids = []

        for rec in inven:
            prod_ids.extend([v.lower() for k, v in rec.items() if k.lower() == 'prod_id'])

        inp = del_prodid_entry.get()

        if inp.lower() not in prod_ids:
            return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')

        if not(messagebox.askyesno(title='CONFIRM DELETE', message='Do You Want To Delete?')):
            return messagebox.showinfo(message='RECORD NOT DELETED')

        for row, rec in lines.items():
            for k, v in rec.items():
                # if valid ID is entered
                if k.lower() == 'prod_id' and v.lower() == inp.lower():
                    del_row = row
                    # print(f"Found at {del_row}")

        with open(Inventory.inv_data, 'w', encoding='utf8') as hand:
            for row, rec in lines.items():
                if row == del_row:
                    # assign the selected row
                    self.inv_obj.__dict__ = rec
                    continue
                hand.writelines(f"{rec}\n")

        tk.Label(self.display_frame, text=f"PRODUCT\n{self.inv_obj.prod_name}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=0, sticky='nsew', padx=25, pady=15)
        tk.Label(self.display_frame, text=f"ID\n{self.inv_obj.prod_id}: ", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=1, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"STOCK:\n{self.inv_obj.qty} {self.inv_obj.unit}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=2, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text=f"DATE:\n{self.inv_obj.entry_date}", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=0, column=3, sticky='nsew', padx=25)
        tk.Label(self.display_frame, text="HAS BEEN DELETED!!", font=("Calibri", 10, 'bold'),
                 bg='purple', fg='white').grid(row=1, column=1, columnspan=2, sticky='NSEW', padx=25)

        invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
                             fg='purple', bg='white', height=1, width=15, command=self.invenpage)
        invpageb.grid(row=2, column=3, padx=5, pady=5, stick='se')

        self.display_frame.rowconfigure([0, 1, 2, 3], weight=1)
        self.display_frame.columnconfigure(list(range(4)), weight=1)
        self.display_frame.grid(row=1, rowspan=len(inven) + 2, column=0, columnspan=4, sticky='nsew')

win = tk.Tk()
# selecting system's screen width height
sw, sh = win.winfo_screenwidth(), win.winfo_screenheight()
# app width, app height
aw, ah = int(sw*.92), int(sh*.7)
# starting horizontal and vertical points
x, y = int(sw*(1 - 0.93)), int(sh*(1 - 0.77))
# specifying the size of app frame
win.geometry(f"{aw}x{ah}+{x}+{y}")

# pass inventory object into the transapp
ta = TransApp(win)

ta.setup_frames()
ta.setup_status_bar()
ta.frontpage()

win.rowconfigure(1, weight=1)
win.columnconfigure(0, weight=1)

win.mainloop()