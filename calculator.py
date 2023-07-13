from tkinter import*

class Calculator:

    def __init__(self, master):

        self.master = master
        master.title("Python Calculator")

        self.equation = Entry(master, width=36, borderwidth=5)
        self.equation.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
         

if __name__=='__main__':

    root = Tk()
    my_gui = Calculator(root)
    root.mainloop()