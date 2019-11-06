import tkinter as tk
from tkinter import messagebox


def open_application():

    window = tk.Tk()
    window.title("Hot Dog World")
    window.tk_setPalette(background='#F8F8F8', foreground='black',
                activeBackground='#C0C0C0', activeForeground='#F8F8F8')

    # create dimentions of window- half of screen width & height
    width = window.winfo_screenwidth()
    height = window.winfo_screenheight()
    window.geometry('%sx%s' % (int(width/1.5), int(height/1.5)))

    # create GUI itself
    cal_profit_date = tk.StringVar()
    tk.Label(window, text="The Hotdog World", font=("Eras Bold ITC", 30), background="#90ee90", width=40,
                  height=2).grid(row=0,columnspan=2)
    tk.Button(window, text="Calculate Total Profit", command=calculate_total_profit).grid(row=1,pady=15)
    tk.Entry(window, textvariable=cal_profit_date).grid(row=2, column=0)
    tk.Button(window, text="Calculate Day Profit", command=lambda: calculate_day_total(cal_profit_date.get())).grid(row=2,column=1)

    window.grid()
    window.mainloop()


def add_sale(num_of_hotdogs, sale_date, price):
    """this will add the sale to the file"""
    success = True
    return success


def calculate_total_profit():
    """reads file and calculates total profit"""
    total_profit = 0
    tk.messagebox.showinfo("Hot Dog World | Total Profit", "The total profits are: " + str(total_profit))
    return total_profit


def calculate_day_total(day):
    """reads file and calculates the total profit for that day"""
    day_total_profit = 0
    tk.messagebox.showinfo("Hot Dog World | Day Total Profit", "The total profits for " + day + " are: " + str(day_total_profit))
    return day_total_profit


open_application()
