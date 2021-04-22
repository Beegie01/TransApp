class Account:
    acct_data = None
    acct_edits = None
    acct_dels = None

    def __init__(self):
        self.date_opened = None
        self.account_id = None
        self.customer_id = None
        self.currency = None
        self.balance = 0

class AcctTrans:
    acctrans_data = None
    acctrans_edits = None
    acctrans_dels = None

    def __init__(self):
        self.trans_id = None
        self.trans_date = None
        self.account_id = None
        self.trans_type = None
        self.amount = None