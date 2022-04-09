from tkinter import *


class GPA():
    def calculate(self, *args):
        self.final = sum(map(int, list(*args)))
        self.average = int(self.final/len(*args))
        self.grade_scored = "PASS" if self.average > 50 else "FAIL"


class Displayed_GPA(GPA):
    def calculate(self, *args):
        super().calculate(args)
        Label(text=f"{self.final}", font="arial 20 bold").place(x=250, y=170)
        Label(text=f"{self.average}", font="arial 20 bold").place(x=250, y=220)
        Label(text=f"{self.grade_scored}",
              font="arial 20 bold").place(x=250, y=270)


class Sub(Label):
    def __init__(self, root, text, font, x, y):
        super().__init__(root, text=text, font=font)
        super().place(x=x, y=y)


root = Tk()
root.title("Grade Calculator")
root.geometry("500x400")


sub_1 = Sub(root, text="Maths", font="arial 20", x=50, y=20)
sub_2 = Sub(root, text="Sciense", font="arial 20", x=50, y=70)
sub_3 = Sub(root, text="Computer", font="arial 20", x=50, y=120)
total_marks = Sub(root, text="Total", font="arial 20", x=50, y=170)
average_marks = Sub(root, text="Average", font="arial 20", x=50, y=220)
grade_scored = Sub(root, text="Grades", font="arial 20", x=50, y=270)

math_marks = StringVar()
sciense_marks = StringVar()
computer_marks = StringVar()

math_value = Entry(root, textvariable=math_marks)
math_value.place(x=250, y=20)
sciense_value = Entry(root, textvariable=sciense_marks)
sciense_value.place(x=250, y=70)
computer_value = Entry(root, textvariable=computer_marks)
computer_value.place(x=250, y=120)

subjects = Displayed_GPA()

Button(text="Calculate", font="arial 15", bg="green",
       bd=5, command=lambda: subjects.calculate(math_value.get(), sciense_value.get(), computer_value.get())).place(x=50, y=330)
Button(text="Exit", font="arial 15", bg="red", bd=5,
       width=8, command=lambda: exit()).place(x=350, y=330)

root.mainloop()
