import tkinter
from tkinter import *

window = Tk()
window.title("BMI Calculator")
window.minsize(width=250,height=250)
window.config(padx=30,pady=30)

my_label = Label(text="Enter Your Weight (kg)")
my_label.pack()

kg = Entry()
kg.pack()


my_label2 = Label(text="Enter Your Height (cm)")
my_label2.pack()


cm = Entry()
cm.pack()


def button_click():
    num1 = kg.get()
    num2 = cm.get()
    if num1 == "" or num2 =="":
        my_label3.config(text="Enter both weight and height")
    else:
        try:
            x = float(num1) / (float(num2) / 100) ** 2
            if x < 18.4:
                result_string = f"Your BMI is : {round(x,2)} You are Under Weight"
                my_label3.config(text=result_string)
            elif 18.5 < x < 24.9:
                result_string = f"Your BMI is : {round(x,2)} You are Normal Weight"
                my_label3.config(text=result_string)
            elif 25.0 < x < 29.9:
                result_string = f"Your BMI is : {round(x,2)} You are Over Weight"
                my_label3.config(text=result_string)
            elif 30 < x <34.9:
                result_string = f"Your BMI is : {round(x,2)} You are Obesity Class 1"
                my_label3.config(text=result_string)
            elif 35 < x <39.9:
                result_string = f"Your BMI is : {round(x,2)} You are Obesity Class 2"
                my_label3.config(text=result_string)
            elif x < 40:
                result_string = f"Your BMI is : {round(x,2)} You are Obesity Class 3"
                my_label3.config(text=result_string)
        except:
            my_label3.config(text="Enter a valid number")



my_button = Button(text="Calculate",command=button_click)
my_button.pack()


my_label3 = Label()
my_label3.pack()




tkinter.mainloop()


