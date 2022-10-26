from tkinter import *
import tkinter.messagebox
from decimal import Decimal

win = Tk()
win.title("calculator")
win.geometry("400x430")
win.resizable(width=False, height=False)
win.configure(bg="#0086FF")

res = StringVar()

frm1 = Frame(win, width=400, height=100, bg="#0086FF")
frm1.pack(side=TOP, pady=10)

frm2 = Frame(win, width=100, height=400, bg="#0086FF")
frm2.pack(side=LEFT, padx=2)

frm3 = Frame(win, width=100, height=400, bg="#0086FF")
frm3.pack(side=LEFT)

frm4 = Frame(win, width=100, height=400, bg="#0086FF")
frm4.pack(side=LEFT, padx=1)

frm5 = Frame(win, width=100, height=400, bg="#0086FF")
frm5.pack(side=LEFT)

lbl_1 = Label(
    frm1,
    width=400,
    height=4,
    textvariable=res,
    bg="white",
    font=("Courier", 20),
    relief=GROOVE
)
lbl_1.pack(side=TOP, padx=5, pady=12)


class claculator:
    def __init__(self):
        self.stack = list()
        self.num_str = ""
        self.show_str = ""
        self.check_dot = False

    def dot(self):
        if self.check_dot == False:
            if self.num_str == "":
                self.num_str = "0."
                self.show_str += "0."
            else:
                self.num_str += "."
                self.show_str += "."
            self.check_dot = True
            res.set(self.show_str)
        else:
            tkinter.messagebox.showerror("ERROR", "You cant use dot here.")

    def operation(self, oper):
        if self.num_str == "":
            if oper == "-":
                self.stack.append(Decimal(-1.0))
                self.stack.append("*")
                self.show_str = self.show_str + "(-1.0)*"
                res.set(self.show_str)
            else:
                tkinter.messagebox.showerror("ERROR", "You must enter number.")
        else:
            self.stack.append(Decimal(self.num_str))
            self.num_str = ""
            self.stack.append(oper)
            self.show_str = self.show_str + oper
            self.check_dot = False
            res.set(self.show_str)

    def nums(self, num):
        self.num_str += num
        self.show_str += num
        res.set(self.show_str)

    def clear(self):
        self.show_str = ""
        self.num_str = ""
        self.stack = []
        self.check_dot = False
        res.set(self.show_str)

    def res(self):
        if self.num_str == "":
            tkinter.messagebox.showerror("ERROR", "You must enter number.")
        else:
            self.stack.append(Decimal(self.num_str))
            self.num_str = ""
            while len(self.stack) > 1:
                a = Decimal(self.stack.pop())
                oper1 = self.stack.pop()
                b = Decimal(self.stack.pop())
                oper2 = ""
                if len(self.stack) > 1:
                    oper2 = self.stack.pop()
                    c = Decimal(self.stack.pop())
                if oper1 == "*":
                    if oper2 != "":
                        self.stack.append(c)
                        self.stack.append(oper2)
                    self.stack.append(a * b)
                elif oper1 == "/":
                    if oper2 != "":
                        self.stack.append(c)
                        self.stack.append(oper2)
                    self.stack.append(b / a)
                elif oper1 == "+":
                    if oper2 == "*":
                        self.stack.append(c * b)
                        self.stack.append(oper1)
                        self.stack.append(a)
                    elif oper2 == "/":
                        self.stack.append(c / b)
                        self.stack.append(oper1)
                        self.stack.append(a)
                    else:
                        if oper2 != "":
                            self.stack.append(c)
                            self.stack.append(oper2)
                        self.stack.append(a + b)
                elif oper1 == "-":
                    if oper2 == "*":
                        self.stack.append(c * b)
                        self.stack.append(oper1)
                        self.stack.append(a)
                    elif oper2 == "/":
                        self.stack.append(c / b)
                        self.stack.append(oper1)
                        self.stack.append(a)
                    else:
                        if oper2 != "":
                            self.stack.append(c)
                            self.stack.append(oper2)
                        self.stack.append(b - a)
            if self.stack[0] % 1 != 0:
                self.check_dot = True
            else:
                self.check_dot = False
            if self.stack[0] == -0:
                self.stack[0] = 0
            self.show_str = str(self.stack[0])
            self.num_str = str(self.stack[0])
            self.stack = []

        res.set(self.show_str)


cal = claculator()

div_btn = Button(frm5, text="/", width=12, height=2, font=("Courier", 11), bg="grey",
                 command=lambda: cal.operation("/"), cursor="hand2")
div_btn.pack(side=TOP, padx=3, pady=2)

mul_btn = Button(frm5, text="*", width=12, height=2, font=("Courier", 11), bg="grey",
                 command=lambda: cal.operation("*"), cursor="hand2")
mul_btn.pack(side=TOP, padx=3, pady=2)

minus_btn = Button(frm5, text="-", width=12, height=2, font=("Courier", 10), bg="grey",
                   command=lambda: cal.operation("-"), cursor="hand2")
minus_btn.pack(side=TOP, padx=3, pady=2)

plus_btn = Button(frm5, text="+", width=12, height=2, font=("Courier", 10), bg="grey",
                  command=lambda: cal.operation("+"), cursor="hand2")
plus_btn.pack(side=TOP, padx=3, pady=2)

dot_btn = Button(frm5, text=".", width=12, height=2, font=("Courier", 10), bg="grey", command=lambda: cal.dot(),
                 cursor="hand2")
dot_btn.pack(side=TOP, padx=3, pady=2)

nine_btn = Button(frm4, text="9", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("9"), cursor="hand2")
nine_btn.pack(side=TOP, padx=2, pady=3)

six_btn = Button(frm4, text="6", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("6"), cursor="hand2")
six_btn.pack(side=TOP, padx=2, pady=3)

three_btn = Button(frm4, text="3", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("3"), cursor="hand2")
three_btn.pack(side=TOP, padx=2, pady=3)

res_btn = Button(frm4, text="=", width=12, height=3, bg="#48DED5", command=lambda: cal.res(), cursor="hand2")
res_btn.pack(side=TOP, padx=2, pady=3)

eight_btn = Button(frm3, text="8", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("8"), cursor="hand2")
eight_btn.pack(side=TOP, padx=2, pady=3)

five_btn = Button(frm3, text="5", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("5"), cursor="hand2")
five_btn.pack(side=TOP, padx=2, pady=3)

two_btn = Button(frm3, text="2", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("2"), cursor="hand2")
two_btn.pack(side=TOP, padx=2, pady=3)

zero_btn = Button(frm3, text="0", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("0"), cursor="hand2")
zero_btn.pack(side=TOP, padx=2, pady=3)

seven_btn = Button(frm2, text="7", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("7"), cursor="hand2")
seven_btn.pack(side=TOP, padx=2, pady=3)

four_btn = Button(frm2, text="4", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("4"), cursor="hand2")
four_btn.pack(side=TOP, padx=2, pady=3)

one_btn = Button(frm2, text="1", width=12, height=3, bg="#D5CABD", command=lambda: cal.nums("1"), cursor="hand2")
one_btn.pack(side=TOP, padx=2, pady=3)

clear_btn = Button(frm2, text="C", width=12, height=3, bg="#48DED5", command=lambda: cal.clear(), cursor="hand2")
clear_btn.pack(side=TOP, padx=2, pady=3)

win.mainloop()
