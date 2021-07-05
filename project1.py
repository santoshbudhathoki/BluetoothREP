from tkinter import *
from tkinter import ttk
import bluetooth
import bluetooth as bt

class scanner:
    def __init__(self,window):
        self.window = window
        self.window.title("Bluetooth Scanner")
        self.window.geometry('550x440+0+0')
        devices = bluetooth.discover_devices(lookup_names=True)
        def func():
            pr = print(devices)
            for i in devices:
                self.tree_view.insert("", "end", text=(i[0],i[1]), value=(i[0],i[1]))
                # self.tree_view.insert("", "end", text=i[1], value=)
        self.scan=Button(self.window,borderwidth=0,text="scan",command=func)
        self.scan.grid(row = 0, column = 2)


        self.tree_view = ttk.Treeview(self.window, columns=('MAC','Names'))
        self.tree_view.place(x=24,y=110,width=460,height=240)
        self.tree_view['show'] = 'headings'
        self.tree_view.column('MAC', width=150)
        self.tree_view.column('Names', width=100)

        self.tree_view.heading('MAC', text="MAC Address")
        self.tree_view.heading('Names', text="Device Names")



def main():
    tks = Tk()
    obj = scanner(tks)
    tks.mainloop()
if __name__ == '__main__':
    main()
# jkkl