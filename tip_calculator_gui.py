import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import *


class AppFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.billAmount = tk.StringVar()
        self.tipPercentage = tk.StringVar()
        self.noOfPeoples = tk.StringVar()

        self.billAmount_Label = ttk.Label(
            self, text="Enter the Bill Amount:").pack()
        self.billAmount_Entry = ttk.Entry(
            self, textvariable=self.billAmount).pack()

        self.tipPercentage_Label = ttk.Label(
            self, text="Enter the Tip Percentage:").pack()
        self.tipPercentage_Entry = ttk.Entry(
            self, textvariable=self.tipPercentage).pack()

        self.noOfPeoples_Label = ttk.Label(
            self, text="Enter the Number of Peoples:").pack()
        self.noOfPeoples_Entry = ttk.Entry(
            self, textvariable=self.noOfPeoples).pack()

        self.button = ttk.Button(self, text="Calculate")
        self.button['command'] = self.calculateTip_fn
        self.button.pack(expand=True)

        self.totalAmount_Label = ttk.Label(
            self, text="")
        self.totalAmount_Label.pack(expand=True)

        self.totalPerPerson_Label = ttk.Label(
            self, text="")
        self.totalPerPerson_Label.pack(expand=True)

        self.pack(expand=True)

    def calculateTip_fn(self):
        if self.billAmount.get() == "" or self.tipPercentage.get() == "" or self.noOfPeoples.get() == "":
            showerror(title="Error", message="Please enter valid number")

        billAmount = float(self.billAmount.get())
        tipPercent = float(self.tipPercentage.get())
        noOfPeoples = int(self.noOfPeoples.get())

        if noOfPeoples < 1:
            showerror(title="Error",
                      message="Number of Peoples must not less than 1")
        else:
            tip = tipPercent/100
            totalTip = billAmount*tip
            totalAmount = billAmount+totalTip
            totalPerPerson = round((totalAmount/noOfPeoples), 2)

            self.totalAmount_Label.config(text=f"Total Amount:{totalAmount}")
            self.totalPerPerson_Label.config(
                text=f"Total Per Person:{totalPerPerson}")


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Tip Calculator')
        self.geometry('500x250')


if __name__ == "__main__":
    app = App()
    frame = AppFrame(app)
    app.mainloop()
