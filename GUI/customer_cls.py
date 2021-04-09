class Customer:
    cust_data = 'C:\\Users\\welcome\\Desktop\\Personal Python Projects\\GUI\\TransApp\\cust_data.txt'

    def __init__(self):#, master):
        # self.master = master
        self.customer_id = None
        self.first_name = None
        self.mid_name = None
        self.last_name = None
        self.gender = None
        self.date_of_birth = None
        self.country = None
        self.state_of_origin = None
        self.office_addr = None
        self.date_opened = None
    #
    # def make_frame(self, page_title=None, background_color='blue', foreground_color='white'):
    #     # specify the frame text, fg, bg
    #     return tk.LabelFrame(self.master, text=page_title, bg=background_color, fg=foreground_color,
    #                          font=('arial black', 12))
    #
    #
    # def custpage(self):
    #     # frame for customer page containing three rows and one column
    #     self.frameinv = tk.LabelFrame(master=self.master, text='CUSTOMER', font=('arial black', 12), bg='blue',
    #                                   fg='white')
    #     self.frameinv.rowconfigure([0, 1, 2, 3], weight=1)
    #     self.frameinv.columnconfigure(0, weight=1)
    #
    #     self.create = tk.Button(self.frameinv, text='ADD NEW CUSTOMER', bg='white', fg='blue',
    #                             font=('arial black', 14), command=self.new_cust)
    #     self.edit = tk.Button(self.frameinv, text='UPDATE CUSTOMER RECORD', bg='white', fg='orange',
    #                           font=('arial black', 14), command=self.edit_cust)
    #     self.dele = tk.Button(self.frameinv, text='DELETE CUSTOMER RECORD', bg='white', fg='red',
    #                           font=('arial black', 14), command=self.delete_cust)
    #     self.view = tk.Button(self.frameinv, text='VIEW CUSTOMER RECORDS', bg='white', fg='green',
    #                           font=('arial black', 14), command=lambda: self.display_cust())
    #
    #     # display inventory options
    #     self.view.grid(row=0, padx=40, pady=10, sticky='nsew')
    #     self.create.grid(row=1, padx=60, pady=10, sticky='nsew')
    #     self.edit.grid(row=2, padx=80, pady=10, sticky='nsew')
    #     self.dele.grid(row=3, padx=100, pady=10, sticky='nsew')
    #
    #     # display inventory page's frame
    #     if self.display_frame is not None:
    #         self.display_frame.grid_forget()
    #     if self.new_prod_frame is not None:
    #         self.new_prod_frame.grid_forget()
    #     if self.frame2 is not None:
    #         self.frame2.grid_forget()
    #
    #     self.frameinv.grid(row=1, rowspan=4, column=0, columnspan=5, sticky='nsew')
    #
    # def new_cust(self):
    #     bg, fg = 'blue', 'white'
    #
    #     # frame for input of new inventory
    #     self.new_prod_frame = tk.LabelFrame(self.master, text='NEW CUSTOMER REGISTRATION', fg=fg,
    #                                         font=('arial black', 12),
    #                                         bg=bg)
    #     self.new_prod_frame.rowconfigure(list(range(9)), weight=1)
    #     self.new_prod_frame.columnconfigure(list(range(5)), weight=1)
    #
    #     # place new customer form
    #     # customer Name
    #     tk.Label(self.new_prod_frame, text='Customer', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=0, column=0, padx=10, stick='nsew')
    #     # first name
    #     tk.Label(self.new_prod_frame, text='First Name', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=0, column=1, stick='nw')
    #     self.fnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
    #     self.fnameEntry.grid(row=0, column=1, padx=2, pady=30, stick='sw')
    #     # middle name
    #     tk.Label(self.new_prod_frame, text='Middle Name', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=0, column=2, stick='nw')
    #     self.midnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
    #     self.midnameEntry.grid(row=0, column=2, padx=2, pady=30, stick='sw')
    #     # last name
    #     tk.Label(self.new_prod_frame, text='Last Name', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=0, column=3, stick='nw')
    #     self.lnameEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'))
    #     self.lnameEntry.grid(row=0, column=3, padx=2, pady=30, stick='sw')
    #
    #     # customer Gender
    #     tk.Label(self.new_prod_frame, text='Gender:', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=1, column=0, padx=10, stick='nsew')
    #     gend = tk.StringVar(value='None')
    #     # gend.set("")
    #     maleRadio = tk.Radiobutton(self.new_prod_frame, text='Male', val='Male', variable=gend, font=('calibri', 16),
    #                                bg='blue', fg='black', command=lambda: self.sel_gender(gend.get()), state='normal')
    #     maleRadio.grid(row=1, column=1, padx=2, sticky='w')
    #     femaleRadio = tk.Radiobutton(self.new_prod_frame, text='Female', val='Female', variable=gend,
    #                                  font=('calibri', 16),
    #                                  bg='blue', fg='black', command=lambda: self.sel_gender(gend.get()), state='normal')
    #     femaleRadio.grid(row=1, column=2, padx=2, sticky='w')
    #
    #     # customer date of birth
    #     tk.Label(self.new_prod_frame, text='Date of Birth:', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=2, column=0, padx=10, stick='nsew')
    #     # day
    #     tk.Label(self.new_prod_frame, text='Day', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=2, column=1, padx=5, stick='nw')
    #     self.bdayEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.bdayEntry.insert(0, str(datetime.date.today().day))
    #     self.bdayEntry.grid(row=2, column=1, padx=5, pady=30, stick='sw')
    #     # month
    #     tk.Label(self.new_prod_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=2, column=2, padx=5, stick='nw')
    #     self.bmonthEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.bmonthEntry.insert(0, str(datetime.date.today().month))
    #     self.bmonthEntry.grid(row=2, column=2, padx=5, pady=30, stick='sw')
    #     # year
    #     tk.Label(self.new_prod_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=2, column=3, stick='nw')
    #     self.byrEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.byrEntry.insert(0, str(datetime.date.today().year))
    #     self.byrEntry.grid(row=2, column=3, pady=30, stick='sw')
    #
    #     # nationality
    #     tk.Label(self.new_prod_frame, text='Nationality:', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=3, column=0, padx=10, stick='nsew')
    #     tk.Label(self.new_prod_frame, text='Country of Origin', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=3, column=1, stick='nw')
    #     self.natEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.natEntry.grid(row=3, column=1, padx=5, pady=30, stick='sw')
    #
    #     # state of origin
    #     tk.Label(self.new_prod_frame, text='State of Origin', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=3, column=2, stick='nw')
    #     self.stateEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.stateEntry.grid(row=3, column=2, padx=5, pady=30, stick='sw')
    #
    #     # Office address
    #     tk.Label(self.new_prod_frame, text='Office Address:', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=4, column=0, padx=5, stick='nsew')
    #     self.off_addrText = tk.Text(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10, height=3)
    #     self.off_addrText.grid(row=4, column=1, padx=5, pady=30, sticky='ew')
    #
    #     # date of registration
    #     tk.Label(self.new_prod_frame, text='As of Date:', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=5, column=0, padx=5, sticky='nsew')
    #     # day
    #     tk.Label(self.new_prod_frame, text='Day', font=('calibri', 16),
    #              bg=bg, fg=fg, height=1).grid(row=5, column=1, sticky='nw')
    #     self.regdayEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.regdayEntry.insert(0, str(datetime.date.today().day))
    #     self.regdayEntry.grid(row=5, column=1, padx=5, pady=30, sticky='sw')
    #     # month
    #     tk.Label(self.new_prod_frame, text='Month', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=5, column=2, sticky='nw')
    #     self.regmonthEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.regmonthEntry.insert(0, str(datetime.date.today().month))
    #     self.regmonthEntry.grid(row=5, column=2, padx=5, pady=30, sticky='sw')
    #     # year
    #     tk.Label(self.new_prod_frame, text='Year', font=('calibri', 16), bg=bg, fg=fg,
    #              height=1).grid(row=5, column=3, sticky='nw')
    #     self.regyrEntry = tk.Entry(self.new_prod_frame, font=('calibri', 16, 'bold'), width=10)
    #     self.regyrEntry.insert(0, str(datetime.date.today().year))
    #     self.regyrEntry.grid(row=5, column=3, pady=30, sticky='sw')
    #
    #     submitButton = tk.Button(self.new_prod_frame, text='Submit', font=("Calibri", 14, 'bold'),
    #                              fg='white', bg='green', width=10, height=2, command=self.submitcust)
    #     submitButton.grid(row=7, column=2, padx=10, sticky='se')
    #
    #     custpageb = tk.Button(self.new_prod_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
    #                           fg='blue', bg='white', height=2, width=15, command=self.custpage)
    #     custpageb.grid(row=7, column=0, padx=15, stick='se')
    #
    #     # display inventory page's frame
    #     if self.submit_frame is not None:
    #         self.submit_frame.grid_forget()
    #     if self.frameinv is not None:
    #         self.frameinv.grid_forget()
    #
    #     self.new_prod_frame.grid(row=1, rowspan=8, column=0, columnspan=3, sticky='nsew')
    #
    # def sel_gender(self, selected_gender):
    #     self.gender = selected_gender
    #     print(self.gender)
    #
    # def submitcust(self):
    #     # frame for submission status
    #     self.submit_frame = tk.LabelFrame(self.master, text='DO YOU WANT TO SAVE?', fg='white',
    #                                       font=('arial black', 12), bg='blue')
    #     self.submit_frame.rowconfigure(list(range(5)), weight=1)
    #     self.submit_frame.columnconfigure(list(range(4)), weight=1)
    #
    #     fname, midname, lname = self.fnameEntry.get(), self.midnameEntry.get(), self.lnameEntry.get()
    #     gender = self.gender
    #     bday, bmon, byr = self.bdayEntry.get(), self.bmonthEntry.get(), self.byrEntry.get()
    #     natn, orig_state = self.natEntry.get(), self.stateEntry.get()
    #     off_addr = self.off_addrText.get(index1='1.0', index2='end')
    #     regday, regmon, regyr = self.regdayEntry.get(), self.regmonthEntry.get(), self.regyrEntry.get()
    #
    #     # collection of entry fields
    #     mandatory_entries = [fname, lname, gender, bday, bmon, byr, natn, orig_state, off_addr, regday, regmon, regyr]
    #     num_type_entries = [bday, bmon, byr, regday, regmon, regyr]
    #     str_type_entries = [fname, midname, lname, gender, natn, orig_state, off_addr]
    #     wspace = string.whitespace  # ['', ' ', '\n', '\t']
    #     puncs = string.punctuation
    #
    #     # check for empty field
    #     if [True for entry in mandatory_entries if (entry in wspace)]:
    #         return messagebox.showerror(title='Blank Field', message='BLANK FIELD(S) DETECTED!')
    #     # check for fields with punctuations
    #     if [True for entry in mandatory_entries if (entry in puncs)]:
    #         return messagebox.showerror(title='Punctuation Error',
    #                                     message='FIELD(S) CANNOT CONTAIN PUNCTUATION MARK(S)!')
    #
    #     # check for fields with invalid data types
    #     for entry in str_type_entries:
    #         try:
    #             float(entry)
    #             # figures have been entered, if no error was raised
    #             return messagebox.showerror(title='Invalid Data Type', message=f'Number {entry} is not allowed here!')
    #         except ValueError as VE:
    #             continue
    #
    #     for entry in num_type_entries:
    #         try:
    #             int(entry)
    #         except ValueError as VE:
    #             # figures have not been entered, if error was raised
    #             return messagebox.showerror(title='Invalid Data Type',
    #                                         message=f'Character {entry} is not allowed here!')
    #
    #     # numerical constraints
    #     if int(byr) not in range(1900, 2021) or (int(regyr) not in range(2010, 2022)) or [True for mon in [regmon, bmon]
    #                                                                                       if int(mon) not in range(
    #                 13)] or [True for day in [bday, regday] if int(day) not in range(32)]:
    #         return messagebox.showerror(title='OUT OF RANGE ENTRY',
    #                                     message=f'OUT OF RANGE VALUE(S) HAS BEEN DETECTED!\n\nPlease Check the REGISTRATION DATE\nDATE OF BIRTH entries')
    #
    #     # string constraints
    #     if [True for entry in [fname, lname, natn, orig_state, ] if not (entry.isalnum)] or [True for entry in
    #                                                                                          [fname, lname, natn,
    #                                                                                           orig_state] for char in
    #                                                                                          entry if
    #                                                                                          char in string.punctuation]:
    #         return messagebox.showerror(title='INVALID CHARACTER',
    #                                     message=f'INVALID CHARACTER HAS BEEN ENTERED!\n\nPlease Check entries:\nFIRST NAME\nLAST NAME\nNATIONALITY')
    #
    #     self.customer_id = f'{natn[0].upper()}{orig_state[:2]}{self.ID_gen()}'
    #     self.first_name, self.last_name = fname, lname
    #     if midname not in wspace:
    #         self.mid_name = midname
    #     self.gender, self.date_of_birth = gender, f"{byr}-{bmon}-{bday}"
    #     self.country, self.state_of_origin = natn, orig_state
    #     self.office_addr, self.date_opened = off_addr, f"{regyr}-{regmon}-{regday}"
    #
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"ID:\n{self.customer_id}").grid(row=0, column=0, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"FIRST NAME\n{self.first_name}").grid(row=0, column=1, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"MIDDLE NAME\n{self.mid_name}").grid(row=0, column=2, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"LAST NAME\n{self.last_name}").grid(row=0, column=3, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"GENDER\n{self.gender}").grid(row=1, column=0, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"DATE OF BIRTH\n{self.date_of_birth}").grid(row=1, column=1, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"NATIONALITY\n{self.country}").grid(row=1, column=2, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"STATE OF ORIGIN\n{self.state_of_origin}").grid(row=1, column=3, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"OFFICE ADDRESS\n{self.office_addr}").grid(row=2, column=0, columnspan=2, sticky='ew')
    #     tk.Label(self.submit_frame, font=("Calibri", 14, 'bold'), bg='blue', fg='white',
    #              text=f"DATE OPENED\n{self.date_opened}").grid(row=2, column=2, sticky='ew')
    #
    #     # save and cancel buttons
    #     saveb = tk.Button(self.submit_frame, text='Save', font=("Calibri", 14, 'bold'),
    #                       bg='green', fg='white', height=3, width=10, command=self.savecust)
    #     saveb.grid(row=4, column=0, padx=5, stick='ew')
    #     cancelb = tk.Button(self.submit_frame, text='Cancel', font=("Calibri", 14, 'bold'),
    #                         bg='red', fg='white', height=3, width=10, command=self.new_cust)
    #     cancelb.grid(row=4, column=3, padx=5, stick='ew')
    #
    #     if self.display_frame is not None:
    #         self.display_frame.grid_forget()
    #     if self.new_prod_frame is not None:
    #         self.new_prod_frame.grid_forget()
    #
    #     self.submit_frame.grid(row=1, sticky='nsew')
    #
    # def savecust(self):
    #     with open(self.cust_data, 'a',
    #               encoding='utf8') as hand:
    #         hand.writelines(f"{self.__dict__}\n")
    #
    #     self.submit_frame = self.make_frame(background_color='blue')
    #
    #     saved = tk.Label(self.submit_frame, text='NEW CUSTOMER HAS BEEN ADDED!', font=("arial", 14, 'bold'),
    #                      bg='blue', fg='white')
    #     saved.grid(row=0, column=0, columnspan=4, sticky='nsew')
    #
    #     addb = tk.Button(self.submit_frame, text='Add Another', font=("Calibri", 14, 'bold'),
    #                      fg='blue', bg='white', height=5, width=15, command=self.new_cust)
    #     addb.grid(row=1, column=0, padx=5, stick='ew')
    #
    #     custpageb = tk.Button(self.submit_frame, text='Customer Page', font=("Calibri", 14, 'bold'),
    #                           bg='blue', fg='white', height=5, width=15, command=self.custpage)
    #     custpageb.grid(row=1, column=3, padx=5, stick='ew')
    #
    #     self.submit_frame.rowconfigure([0, 1], weight=1)
    #     self.submit_frame.columnconfigure(list(range(4)), weight=1)
    #     self.submit_frame.grid(row=1, sticky='nsew')
    #
    # def read_cust(self):
    #     with open(self.cust_data, 'r', encoding='utf8') as hand:
    #         # customer attributes is a list of record strings
    #         cust_attr = hand.readlines()
    #     return cust_attr
    #
    # def display_cust(self):
    #     global cust, lines
    #     cust = []
    #     lines = {}
    #
    #     # setup display frame
    #     self.display_frame = self.make_frame(page_title='CUSTOMER RECORDS VIEW', background_color='blue')
    #
    #     # retrieve customer data from file
    #     # cust is a list of strings containing customer records
    #     cust_rec = self.read_cust()
    #
    #     for ind in range(len(cust_rec)):
    #         # labelled format of saved customer record
    #         lines['Row_' + str(ind)] = eval(cust_rec[ind])
    #         # cust is a list of saved customer instances
    #         cust.append(eval(cust_rec[ind]))
    #
    #     # display headings for customer records
    #     tk.Label(self.display_frame, text="CUSTOMER ID", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=0, sticky='e')
    #     tk.Label(self.display_frame, text="CUSTOMER NAME", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=1, sticky='nsew')
    #     tk.Label(self.display_frame, text="GENDER", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=2, sticky='nsew')
    #     tk.Label(self.display_frame, text="DATE OF BIRTH", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=3, sticky='nsew')
    #     tk.Label(self.display_frame, text="NATIONALITY", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=4, sticky='nsew')
    #     tk.Label(self.display_frame, text="STATE OF ORIGIN", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=5, sticky='nsew')
    #     tk.Label(self.display_frame, text="OFFICE ADDRESS", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=6, sticky='nsew')
    #     tk.Label(self.display_frame, text="DATE OPENED", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, column=7, sticky='nsew')
    #
    #     for ind in range(len(cust)):
    #         # assign user input from stored customer records to each customer class attribute
    #         self.__dict__ = cust[ind]
    #
    #         tk.Label(self.display_frame, text=f"{self.customer_id}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=0, sticky='e')
    #         tk.Label(self.display_frame,
    #                  text=f"{self.first_name} {self.mid_name} {self.last_name}",
    #                  font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=1, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.gender}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=2, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.date_of_birth}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=3, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.country}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=4, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.state_of_origin}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=5, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.office_addr}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=6, sticky='nsew')
    #         tk.Label(self.display_frame, text=f"{self.date_opened}", font=("Calibri", 10, 'bold'),
    #                  bg='blue', fg='white').grid(row=ind + 1, column=7, sticky='nsew')
    #
    #     custpageb = tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
    #                           fg='blue', bg='white', height=1, width=15, command=self.custpage)
    #     custpageb.grid(row=len(cust) + 2, column=3, padx=5, pady=5, stick='se')
    #
    #     if self.submit_frame is not None:
    #         self.submit_frame.grid_forget()
    #     if self.edit_prod_frame is not None:
    #         self.edit_prod_frame.grid_forget()
    #     if self.new_prod_frame is not None:
    #         self.new_prod_frame.grid_forget()
    #
    #     self.display_frame.rowconfigure(list(range(len(cust) + 2)), weight=1)
    #     self.display_frame.columnconfigure(list(range(9)), weight=1)
    #     self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')
    #
    # def edit_cust(self):
    #     global edit_custid_entry, cust, lines
    #     cust = []
    #     lines = {}
    #
    #     # setup display frame
    #     self.display_frame = self.make_frame(page_title='CUSTOMER RECORDS VIEW', background_color='blue')
    #
    #     # retrieve customer data from file
    #     # cust is a list of strings containing customer records
    #     cust_rec = self.read_cust()
    #
    #     for ind in range(len(cust_rec)):
    #         # labelled format of saved customer record
    #         lines['Row_' + str(ind)] = eval(cust_rec[ind])
    #         # cust is a list of saved customer instances
    #         cust.append(eval(cust_rec[ind]))
    #
    #     # display headings for customer records
    #     # create scrolled text field to display customer records
    #     st = scrolledtext.ScrolledText(self.display_frame, bg='blue', fg='white', wrap='word',
    #                                    font=("Calibri", 14, 'bold'))
    #     st.grid(row=0, column=0, rowspan=len(cust), columnspan=8, sticky='nsew')
    #     # display headings for customer records
    #     st.insert(index='end',
    #               chars='CUSTOMER ID, FIRST NAME, MIDDLE NAME, LAST NAME, GENDER, DATE OF BIRTH, NATIONALITY, STATE OF ORIGIN, OFFICE ADDRESS, DATE OPENED\n\n')
    #
    #     for ind in range(len(cust)):
    #         # assign user input from stored customer records to each customer class attribute
    #         self.__dict__ = cust[ind]
    #
    #         st.insert(index='end',
    #                   chars=f"{self.customer_id}, {self.first_name}, {self.mid_name}, {self.last_name}, {self.gender}, {self.date_of_birth}, {self.country}, {self.state_of_origin}, {' '.join(self.office_addr.split())}, {self.date_opened}\n\n")
    #     # make text field read-only
    #     st.config(state='disabled')
    #     # ensure that text can be copied to clipboard
    #     st.bind('<1>', lambda event: st.focus_set())
    #
    #     # to edit the given row number (at row entry - 1)
    #     tk.Label(self.display_frame, text='ENTER CUSTOMER ID:', font=("Calibri", 12, 'bold'), bg='blue',
    #              fg='white').grid(row=len(cust) + 2, column=0, padx=2, sticky='e')
    #     # custid entry
    #     edit_custid_entry = tk.Entry(self.display_frame, font=("Calibri", 12, 'bold'), relief='sunken')
    #     edit_custid_entry.grid(row=len(cust) + 2, column=1, padx=2, sticky='ew')
    #     # edit button
    #     tk.Button(self.display_frame, text='Edit', font=("Calibri", 12, 'bold'),
    #               bg='orange', fg='white', height=1, width=10, command=self.editing_cust).grid(row=len(cust) + 2,
    #                                                                                            padx=5, column=2,
    #                                                                                            sticky='w')
    #
    #     custpageb = tk.Button(self.display_frame, text='Customer Page', font=("Calibri", 12, 'bold'),
    #                           fg='blue', bg='white', height=1, width=15, command=self.custpage)
    #     custpageb.grid(row=len(cust) + 2, column=6, padx=5, pady=5, stick='se')
    #
    #     if self.submit_frame is not None:
    #         self.submit_frame.grid_forget()
    #     if self.edit_prod_frame is not None:
    #         self.edit_prod_frame.grid_forget()
    #     if self.new_prod_frame is not None:
    #         self.new_prod_frame.grid_forget()
    #
    #     self.display_frame.rowconfigure(list(range(len(cust) + 2)), weight=1)
    #     self.display_frame.columnconfigure(list(range(9)), weight=1)
    #     self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')
    #
    # def editing_cust(self):
    #     global edit_custid_entry, cust, lines, edit_row
    #
    #     self.display_frame = self.make_frame(page_title='UPDATING INVENTORY RECORD')
    #
    #     customer_ids = []
    #
    #     for rec in cust:
    #         # list of all existing customer ids (converted to lower case)
    #         customer_ids.extend([v.lower() for k, v in rec.items() if k.lower() == 'customer_id'])
    #
    #     inp = edit_custid_entry.get()
    #
    #     if inp.lower() not in customer_ids:
    #         return messagebox.showerror(title='INVALID ENTRY', message=f'{inp} IS NOT VALID')
    #
    #     # get the row index of the selected customer id
    #     for row, rec in lines.items():
    #         for k, v in rec.items():
    #             # if valid ID is entered
    #             if k.lower() == 'customer_id' and v.lower() == inp.lower():
    #                 edit_row = row
    #                 # print(f"Found at {edit_row}")
    #
    #     # assign the selected record to the customer object
    #     for row, rec in lines.items():
    #         if row == edit_row_num:
    #             self.__dict__ = rec
    #     print(self.__dict__)
    #     tk.Label(self.display_frame, text="SELECTED DATA", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=0, columnspan=3, sticky='ew', padx=50)
    #
    #     tk.Label(self.display_frame, text=f"ID:\n\n{self.customer_id}: ", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=1, column=0, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"FIRST NAME:\n\n{self.first_name}", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=1, column=1, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"MIDDLE NAME:\n\n{self.mid_name}", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=1, column=2, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"LAST NAME:\n\n{self.last_name}",
    #              font=("Calibri", 10, 'bold'), bg='blue', fg='white').grid(row=1, column=3, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"GENDER\n\n{self.gender}", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=1, column=4, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"DATE OF BIRTH\n\n{self.date_of_birth}",
    #              font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=2, column=0, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"COUNTRY\n\n{self.country}",
    #              font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=2, column=1, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"STATE OF ORIGIN\n\n{self.state_of_origin}",
    #              font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=2, column=2, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"OFFICE ADDRESS\n\n{self.state_of_origin}",
    #              font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=2, column=3, sticky='ew', padx=25)
    #     tk.Label(self.display_frame, text=f"DATE OPENED\n\n{self.state_of_origin}",
    #              font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=2, column=4, sticky='ew', padx=25)
    #
    #     # entry fields for new data
    #     tk.Label(self.display_frame, text=f"ENTER NEW DATA BELOW", font=("Calibri", 14, 'bold'),
    #              bg='blue', fg='white').grid(row=2, columnspan=3, sticky='ew', padx=50)
    #
    #     # customer labels and entries
    #     tk.Label(self.display_frame, text=f"PRODUCT:", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=3, column=0, sticky='ew', padx=50, pady=15)
    #
    #     # customer name label and entry
    #     tk.Label(self.display_frame, text=f"NAME", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=3, column=1, sticky='nw', padx=25, pady=15)
    #     self.pname_entry = tk.Entry(self.display_frame)
    #     self.pname_entry.grid(row=3, column=1, sticky='w', padx=25, pady=5)
    #
    #     # customer quantity label and entry
    #     tk.Label(self.display_frame, text=f"QUANTITY", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=3, column=2, sticky='nw', padx=25, pady=15)
    #     self.pqty_entry = tk.Entry(self.display_frame)
    #     self.pqty_entry.grid(row=3, column=2, sticky='w', padx=25, pady=5)
    #
    #     # unit of measurement label and entry
    #     tk.Label(self.display_frame, text=f"Unit of Measurement", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=3, column=3, sticky='nw', padx=25, pady=15)
    #     self.punit_entry = tk.Entry(self.display_frame)
    #     self.punit_entry.grid(row=3, column=3, sticky='w', padx=25, pady=5)
    #
    #     # date labels and entries section
    #     tk.Label(self.display_frame, text=f"DATE", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=4, column=0, sticky='ew', padx=25, pady=15)
    #     # Year label and entry
    #     tk.Label(self.display_frame, text=f"YEAR", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=4, column=1, sticky='nw', padx=25, pady=15)
    #     self.yr_entry = tk.Entry(self.display_frame)
    #     self.yr_entry.grid(row=4, column=1, sticky='w', padx=25, pady=5)
    #     # Month label and entry
    #     tk.Label(self.display_frame, text=f"MONTH", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=4, column=2, sticky='nw', padx=25, pady=15)
    #     self.mon_entry = tk.Entry(self.display_frame)
    #     self.mon_entry.grid(row=4, column=2, sticky='w', padx=25, pady=5)
    #     # Day label and entry
    #     tk.Label(self.display_frame, text=f"DAY", font=("Calibri", 10, 'bold'),
    #              bg='blue', fg='white').grid(row=4, column=3, sticky='nw', padx=25, pady=15)
    #     self.day_entry = tk.Entry(self.display_frame)
    #     self.day_entry.grid(row=4, column=3, sticky='w', padx=25, pady=5)
    #
    #     # update and customer page buttons
    #     updateb = tk.Button(self.display_frame, text='Update', font=("Calibri", 12, 'bold'),
    #                         bg='orange', fg='white', height=1, width=15, command=self.update)
    #     updateb.grid(row=len(cust) + 2, column=1, padx=5, pady=5, stick='sw')
    #
    #     invpageb = tk.Button(self.display_frame, text='Inventory Page', font=("Calibri", 12, 'bold'),
    #                          fg='purple', bg='white', height=1, width=15, command=self.custpage)
    #     invpageb.grid(row=len(cust) + 2, column=3, padx=5, pady=5, stick='sw')
    #
    #     # clear the frames before and after this page
    #     if self.submit_frame is not None:
    #         self.submit_frame.grid_forget()
    #     if self.edit_prod_frame is not None:
    #         self.edit_prod_frame.grid_forget()
    #     if self.new_prod_frame is not None:
    #         self.new_prod_frame.grid_forget()
    #
    #     # display an adjustible frame containing the selected info
    #     self.display_frame.rowconfigure([0, 1, 2, 3, 4], weight=1)
    #     self.display_frame.columnconfigure(list(range(4)), weight=1)
    #     self.display_frame.grid(row=1, rowspan=len(cust) + 2, column=0, columnspan=4, sticky='nsew')
    #
    # def delete_cust(self):
    #     pass
