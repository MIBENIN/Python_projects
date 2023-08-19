from tkinter import ttk
import tkinter as tk


class appFrame(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)
        self.create_widgets()

    def create_widgets(self):
        self.display = ttk.Entry(
            self, text="0", justify="right", foreground="Blue", font=('Bodoni MT', 18))
        self.display['state'] = "disabled"
        self.display.grid(row=0, column=0, columnspan=4,
                          sticky=tk.EW)

        self.btn_AC = ttk.Button(
            self, text="AC", command=self.clearDisplay).grid(row=1, column=0)
        self.btn_Lpara = ttk.Button(
            self, text="(", command=lambda: self.button_clicked("(")).grid(row=1, column=1)
        self.btn_Rpara = ttk.Button(self, text=")", command=lambda: self.button_clicked(")")).grid(
            row=1, column=2)
        self.btn_divide = ttk.Button(
            self, text="/", command=lambda: self.button_clicked("/")).grid(row=1, column=3)

        self.btn_seven = ttk.Button(
            self, text="7", command=lambda: self.button_clicked("7")).grid(row=2, column=0)
        self.btn_eight = ttk.Button(
            self, text="8", command=lambda: self.button_clicked("8")).grid(row=2, column=1)
        self.btn_nine = ttk.Button(
            self, text="9", command=lambda: self.button_clicked("9")).grid(row=2, column=2)
        self.btn_mutiply = ttk.Button(
            self, text="*", command=lambda: self.button_clicked("*")).grid(row=2, column=3)

        self.btn_four = ttk.Button(
            self, text="4", command=lambda: self.button_clicked("4")).grid(row=3, column=0)
        self.btn_five = ttk.Button(
            self, text="5", command=lambda: self.button_clicked("5")).grid(row=3, column=1)
        self.btn_six = ttk.Button(
            self, text="6", command=lambda: self.button_clicked("6")).grid(row=3, column=2)
        self.btn_subtract = ttk.Button(
            self, text="-", command=lambda: self.button_clicked("-")).grid(row=3, column=3)

        self.btn_one = ttk.Button(
            self, text="1", command=lambda: self.button_clicked("1")).grid(row=4, column=0)
        self.btn_two = ttk.Button(
            self, text="2", command=lambda: self.button_clicked("2")).grid(row=4, column=1)
        self.btn_three = ttk.Button(
            self, text="3", command=lambda: self.button_clicked("3")).grid(row=4, column=2)
        self.btn_add = ttk.Button(
            self, text="+", command=lambda: self.button_clicked("+")).grid(row=4, column=3)

        self.btn_zero = ttk.Button(
            self, text="0", command=lambda: self.button_clicked("0")).grid(row=5, column=0)
        self.btn_dot = ttk.Button(
            self, text=".", command=lambda: self.button_clicked(".")).grid(row=5, column=1)
        self.btn_delete = ttk.Button(
            self, text="X", command=self.deleteValue).grid(row=5, column=2)
        self.btn_equalto = ttk.Button(
            self, text="=", command=self.evaluate_expression).grid(row=5, column=3)

        for widget in self.winfo_children():
            widget.grid(ipadx=5, ipady=5, padx=3, pady=3)

        self.grid(padx=10, pady=10, sticky=tk.NSEW)

    def button_clicked(self, text):
        self.display.config(foreground="Blue")
        self.display['state'] = "normal"
        self.display.insert(tk.END, text)
        self.display['state'] = "disabled"

    def deleteValue(self):
        self.display['state'] = "normal"
        self.display.delete(len(self.display.get())-1)
        self.display['state'] = "disabled"

    def clearDisplay(self):
        self.display['state'] = "normal"
        self.display.delete(0, tk.END)
        self.display['state'] = "disabled"

    def is_expression_safe(self, expression):
        allowed_symbols = set("0123456789.+-*/() ")

        try:
            compile(expression, "<string>", "eval")
        except SyntaxError:
            return False

        if not all(char in allowed_symbols for char in expression):
            return False

        return True

    def safe_eval(self, expression):
        if self.is_expression_safe(expression):
            try:
                result = eval(expression)
                return result
            except:
                self.display.config(foreground="Red")
                return "Error during evaluation"
        else:
            self.display.config(foreground="Red")
            return "Invalid or unsafe expression"

    def evaluate_expression(self):
        self.display['state'] = "normal"
        expression = self.display.get()
        result = self.safe_eval(expression)
        self.display.delete(0, tk.END)
        self.display.insert(0, str(result))
        self.display['state'] = "disabled"


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Calculator')
        self.geometry('480x295')
        self.resizable(False, False)
        self.config(bg="blue")
        self.iconbitmap('images\calculator64.ico')


if __name__ == "__main__":
    app = App()
    frame = appFrame(app)
    frame_width = 400
    frame_height = 250
    app.mainloop()
