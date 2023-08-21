import json
import random
import tkinter as tk
from tkinter import ttk

root = tk.Tk()

root.title('Random Quotes Generator')
root.geometry('600x400')
root.resizable(False, False)
root.iconbitmap("images/quote.ico")
root.config(bg="Lightblue")


def GenerateQuotesFn():
    with open('quotes/quotes.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    quotes = data['quotes']
    random_index = random.randint(0, len(quotes) - 1)

    random_quote = quotes[random_index]['quote']
    random_author = quotes[random_index]['author']

    quotes_quote_label.config(text=f"'{random_quote}'")
    quotes_author_label.config(text=f"- {random_author}")


quotes_quote_label = ttk.Label(
    root, text="Whatever the mind of man can conceive and believe, it can achieve.", font=('Impact', 20), wraplength=580, background="Lightblue")
quotes_quote_label.pack(fill='x', padx=10, pady=10)

quotes_author_label = ttk.Label(
    root, text="- Napoleon Hill", font=('Impact', 16), anchor=tk.E, background="Lightblue")
quotes_author_label.pack(fill='x', padx=20, pady=5)

style = ttk.Style()
style.configure("Custom.TButton", font=('Impact', 20))

image = tk.PhotoImage(file='images/random-48.png')
quotes_generator_button = ttk.Button(
    root, text="Generate Quotes", image=image, compound=tk.LEFT, cursor="hand2", style="Custom.TButton")
quotes_generator_button['command'] = GenerateQuotesFn
quotes_generator_button.pack(
    anchor=tk.E, ipadx=5, ipady=5, padx=20, pady=5)

root.mainloop()
