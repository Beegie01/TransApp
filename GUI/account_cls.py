class Account:
    acct_data = None

    def __init__(self):
        self.date_opened = None
        self.account_id = None
        self.customer_id = None
        self.currency = None
        self.balance = None

class AcctTrans:
    acctrans_data = None

    def __init__(self):
        self.trans_date = None
        self.account_id = None
        self.trans_type = None
        self.amount = None