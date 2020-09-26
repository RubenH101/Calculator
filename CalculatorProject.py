from tkinter import*
import math 
cal= Tk()
cal.geometry('442x610')
cal.configure(bg='mediumblue')
cal.title("Calculator")
callabel = Label(cal,text="Calculator",font=('arial',100,'bold'))
def clickbut(numbers):
    current = caltext.get()
    caltext.delete(0, END)
    caltext.insert(0, str(current) + str(numbers))
def button_add():
   first_number = caltext.get()
   global f_num
   global math
   math = "addition"
   f_num = int(first_number)
   caltext.delete(0, END)
def button_subtract():
    first_number = caltext.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_multiply():
    first_number = caltext.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_division():
    first_number = caltext.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_clear():
    caltext.delete(0, END)
def button_sqrt():
    first_number = caltext.get()
    global f_num
    global math
    math = "square root"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_percen():
    first_number = caltext.get()
    global f_num
    global math
    math = "percentage"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_exp():
    first_number = caltext.get()
    global f_num
    global math
    math = "exponent"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_change():
    first_number = caltext.get()
    global f_num
    global math
    math = "change"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_pie():
    first_number = caltext.get()
    global f_num
    global math
    math = "pie"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_2nd():
    first_number = caltext.get()
    global f_num
    global math
    math = "2nd"
    f_num = int(first_number)
    caltext.delete(0, END)
def button_equal():
    second_number = caltext.get()
    caltext.delete(0, END)
    if math == 'addition':
        caltext.insert(0, f_num + int(second_number))
    if math == 'subtraction':
        caltext.insert(0, f_num - int(second_number))
    if math == 'multiplication':
        caltext.insert(0, f_num * int(second_number))
    if math == 'division':
        try:
            caltext.insert(0, f_num / int(second_number))
        except ZeroDivisionError:
            caltext.insert(0, str('ERROR'))
    if math == 'square root':
        caltext.insert(0, f_num ** 0.5)
    if math == 'exponent':
        caltext.insert(0, f_num ** int(second_number))
    if math == 'percentage':
        caltext.insert(0, (f_num * int(second_number))/100)
    if math == 'change':
        caltext.insert(0, f_num / -1)
    if math == 'pie':
        caltext.insert(m.pi)
    if math == '2nd':
        caltext.insert(0, f_num ** 2)
caltext = Entry(cal,width=55,borderwidth=13,font=('oswald',10,'bold'))
caltext.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
but1=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut(1),text='1',font=('oswald',15,'bold')).grid(row=1, column=2)
but2=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut(2),text='2',font=('oswald',15,'bold')).grid(row=2, column=0)
but3=Button(cal,padx=38,pady=10,bd=5,bg='aqua', fg='black',command=lambda:clickbut(3),text='3',font=('oswald',15,'bold')).grid(row=2, column=1)
but4=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut(4),text='4',font=('oswald',15,'bold')).grid(row=2, column=2)
but5=Button(cal,padx=35,pady=10,bd=5,bg='aqua', fg='black',command=lambda:clickbut(5),text='5',font=('oswald',15,'bold')).grid(row=3, column=0)
but6=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut(6),text='6',font=('oswald',15,'bold')).grid(row=3, column=1)
but7=Button(cal,padx=35,pady=10,bd=5,bg='aqua', fg='black',command=lambda:clickbut(7),text='7',font=('oswald',15,'bold')).grid(row=3, column=2)
but8=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut(8),text='8',font=('oswald',15,'bold')).grid(row=4, column=0)
but9=Button(cal,padx=35,pady=10,bd=5,bg='aqua', fg='black',command=lambda:clickbut(9),text='9',font=('oswald',15,'bold')).grid(row=4, column=1)
but0=Button(cal,padx=35,pady=10,bd=5,bg='aqua',command=lambda:clickbut(0),text='0',font=('oswald',15,'bold')).grid(row=1, column=1)
butsub=Button(cal,padx=35,pady=10,bd=5,bg='aqua', fg='black',command=button_subtract,text='-',font=('oswald',15,'bold')).grid(row=6,column=2)
butadd=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=button_add,text='+',font=('oswald',15,'bold')).grid(row=5, column=0)
butmul=Button(cal,padx=35,pady=10,bd=5,bg='aqua', fg='black',command=button_multiply,text='×',font=('oswald',15,'bold ')).grid(row=6,column=0)
butclear=Button(cal,padx=200,pady=15,bd=5,bg='powderblue',command=button_clear,text='CE',font=('oswald',15,'bold')).grid(row=8, column=0, columnspan=4)
butdiv=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue',command=button_division,text='÷',font=('oswald',15,'bold')).grid(row=6, column=1)
butequal=Button(cal,padx=35,pady=250,bd=5,bg='steelblue',fg='white',command=button_equal,text='=',font=('oswald',15,'bold')).grid(row=1, column=3, rowspan=8)
butsqrt=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue',command=button_sqrt,text='√',font=('oswald',15,'bold')).grid(row=7, column=0)
butexp=Button(cal,padx=35,pady=13,bd=5,bg='aqua',command=button_exp,text='xⁿ',font=('oswald',13,'bold')).grid(row=7, column=1)
butpercen=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue',command=button_percen,text='%',font=('oswald',15,'bold')).grid(row=7, column=2)
butplussub=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue',command=button_change,text='±',font=('oswald',15,'bold')).grid(row=4, column=2)
butpie=Button(cal,padx=32,pady=10,bd=5,bg='light blue',command=button_pie,text='π',font=('oswald',15,'bold'))
but2nd=Button(cal,padx=35,pady=12,bd=5,bg='aqua',command=button_2nd,text='x²',font=('oswald',12,'bold')).grid(row=5, column=1)
button_quit=Button(cal,text="EXIT",padx=35, pady=15, bd=10, bg='hotpink', fg='white', command=quit).grid(row=1, column=0)
butdot=Button(cal,padx=35,pady=10,bd=5,bg='deepskyblue', fg='black',command=lambda:clickbut('.'),text='.',font=('oswald',15,'bold')).grid(row=5, column=2)
cal.mainloop()
