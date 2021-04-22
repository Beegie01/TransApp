class User:
    da = 'hello'
    __le = 'Hidden 1'

    def __init__(self):
        self.ha = 'yes'
        self._hal = 'Private'
        self.__hale = 'Hidden 2'

    def access_hidden(self):
        print(self.__le)
        print(self.__dict__)


u = User()
print(u.__dict__)
u.access_hidden()
# print(u._User__hale)
# print(u._User__le)

a = [1, 2, 3]
c = ['f', 'b', 't']
print(*[[k, v] for k, v in zip(a, c)])

import tkinter as tk

def refocus(event):
    root.focus()

root = tk.Tk()
t = tk.Text(root)
t.pack()

t.bind('<Leave>', refocus)
evt1, evt2 = '<Key>', '<Enter><KeyRelease><Leave>'
t.bind(evt1, lambda evt1: print("Typing"))
t.bind(evt2, lambda evt2: print("Finish Typing"))

root.mainloop()