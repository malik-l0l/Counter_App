import random
from tkinter import *

# ---------CONSTANTS------------------
# you can add more colors if you want
colors = ['yellow',
          'white',
          'dark grey',
          'light blue',
          'black',
          'light pink',
          'orange',
          'gold',
          'red',
          'cyan',
          ]


# -------END CONSTANTS----------------

# ---------METHODS------------------------------------------
# you can extra function to prevent the occurrence of same background and foreground color :)
def add():
    """
    increment the counter and change the background color
    :return: None
    """
    count.set(count.get() + 1)
    label_1.config(bg=random.choice(colors))


def subtract():
    """
    decrement the counter if (count > 0) and change text color
    :return: None
    """

    if count.get() != 0:
        count.set(count.get() - 1)
        label_1.config(fg=random.choice(colors))


# ---------END METHODS--------------------------------------

# =============MAIN WINDOW========================================
window = Tk()
window.title("Counter")
window.geometry("400x370")
window.resizable(False, False)

count = IntVar()

label_1 = Label(window,
                font=("Arial", 40, "bold"),
                foreground='red',
                background='white',
                height=5,
                width=15,
                relief=RAISED,
                bd=5,
                textvariable=count
                )
label_1.pack()

Button(window,
       width=14,
       text="-",
       font=("Sans serif", 15, "bold"),
       relief=RAISED,
       bd=5,
       padx=10,
       background='gold',
       command=subtract
       ).pack(side=LEFT)

Button(window,
       width=14,
       text="+",
       font=("Arial", 15, "bold"),
       relief=RAISED,
       bd=5,
       padx=10,
       background='gold',
       command=add,
       ).pack(side=LEFT)

window.mainloop()
# =============END MAIN WINDOW====================================
