class Sales:
    sales_data = None
    sales_edits = None
    sales_dels = None

    def __init__(self):#, master):
        # self.master = master
        self.ord_date = None  # automatic - current date
        self.ord_time = None  # automatic - current time
        self.ord_id = None  # automatic - generated based on date
        self.product_id = None  # selection
        self.customer_id = None  # selection
        self.account_id = None  # selection
        self.ord_quantity = None  # numeric input
        self.ord_unit = None  # automatic generated from account id
        self.rate_per_unit = None  # numeric input
        self.price = None  # automatic generated computation
        self.payment_status = None  # automatic selection
        self.date_of_completion = None  # automatic - current date
        self.date_of_cancellation = None  # automatic - current date