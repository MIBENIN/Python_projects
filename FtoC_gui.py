import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showerror


class AppFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

        self.fahValue = tk.StringVar()

        self.app_label = ttk.Label(
            self, text="Fahrenheit to Degree Conventer").pack(expand=True)

        self.value_label = ttk.Label(self, text="Enter the fahrenheit value(F):", font=(
            'Calibri', 15)).pack(expand=True)

        self.value_entry = ttk.Entry(
            self, textvariable=self.fahValue).pack(expand=True)

        self.button = ttk.Button(self, text="Submit")
        self.button['command'] = self.button_submit_fn
        self.button.pack(expand=True)

        self.result_label = ttk.Label(
            self, text="Result")
        self.result_label.pack(expand=True)
        self.pack(expand=True)

    def fahrenheitToCelsuis(self, f):
        return (f - 32) * 5/9

    def button_submit_fn(self):
        try:
            f = float(self.fahValue.get())
            c = self.fahrenheitToCelsuis(f)
            result = f'{f} Fahrenheit = {c:.2f} Celsius'
            self.result_label.config(text=result)
        except ValueError as error:
            showerror(title='Error', message=error)


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('class demo')
        self.geometry('400x200')
        self.config(bg="Lightblue")


if __name__ == "__main__":
    app = App()
    frame = AppFrame(app)
    app.mainloop()
