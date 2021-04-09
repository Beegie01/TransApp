import os


class User:

    dir_path = f'{os.getcwd()}\\TransAppUsers'
    usernames = []
    master = None
    frame = None

    def __init__(self):
        # User.master = master
        self.email = None
        self.username = None
        self.password = None
        self.company_name = None
        self.filepath = None
