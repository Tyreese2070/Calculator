#Tyreese June 2018

from tkinter import *
import random

root = Tk()
root.title("Calculator")
root.geometry("379x443")

en = Entry(root, width=50)
en.grid(row = 0, column = 0, columnspan = 4, padx=20, pady=20)



#functions
def numberinput(number):
    current = en.get()
    en.delete(0, END)
    en.insert(0, str(current) + str(number))
    
def clearinput():
    en.delete(0, END)
    memory1 = 0
     
def deleteinput():
    value = int(str(en.get()).rstrip())
    en.delete(0, END)
    en.insert(0, value)
    
    
def squarenumber():
    rt = float(en.get())
    rt2 = rt * rt
    en.delete(0, END)
    en.insert(0, str(rt2))
    
def closeapp():
    root.destroy()
    
def numbermultiply():
    first_num = en.get()
    global memory1
    global math
    math = "multiplication"
    memory1 = float(first_num)
    en.delete(0, END)
    print(memory1)
    
def numbersubtract():
    first_num = en.get()
    global memory1
    global math
    math = "subtraction"
    memory1 = float(first_num)
    en.delete(0, END)
    print(memory1)
    
def numberadd():
    first_num = en.get()
    global memory1
    global math
    math = "addition"
    memory1 = float(first_num)
    en.delete(0, END)
    print(memory1)
    
def numbercalc():
    second_num = en.get()
    en.delete(0, END)
    if math == "addition":
        en.insert(0, memory1 + float(second_num))
    elif math == "division":
        en.insert(0, memory1 / float(second_num))
    elif math == "subtraction":
        en.insert(0, memory1 - float(second_num))
    elif math == "multiplication":
        en.insert(0, memory1 * float(second_num))
    print("value of calculation = " + en.get())
    global answer
    answer = en.get()
        
def numberdivide():
    first_num = en.get()
    global memory1
    global math
    math = "division"
    memory1 = float(first_num)
    en.delete(0, END)
    print(memory1)

def sqrtnumber():
    sqrtd = 0
    sqrtd = float(en.get()) ** 0.5
    en.delete(0, END)
    en.insert(0, sqrtd)

def ansinput():
    en.insert(0, answer)

def colourchange():
    print("colour change")
    randomcolour = random.randint(1,5)
    print (randomcolour)
    if randomcolour == "1":
        print("1")

def piinput():
    pinum = 3.141592653589793
    en.insert(0, pinum)
    
        
    
#coding the button

button1 = Button(root, text="1", padx=40, pady=20, command = lambda: numberinput(1))
button2 = Button(root, text="2", padx=40, pady=20, command = lambda: numberinput(2))
button3 = Button(root, text="3", padx=40, pady=20, command = lambda: numberinput(3))

button4 = Button(root, text="4", padx=40, pady=20, command = lambda: numberinput(4))
button5 = Button(root, text="5", padx=40, pady=20, command = lambda: numberinput(5))
button6 = Button(root, text="6", padx=40, pady=20, command = lambda: numberinput(6))

button7 = Button(root, text="7", padx=40, pady=20, command = lambda: numberinput(7))
button8 = Button(root, text="8", padx=40, pady=20, command = lambda: numberinput(8))
button9 = Button(root, text="9", padx=40, pady=20, command = lambda: numberinput(9))

button0 = Button(root, text="0", padx=40, pady=20, command = lambda: numberinput(0))
buttondecpoint = Button(root, text=".", padx=41, pady=20, command = lambda: numberinput("."))
buttonsquare = Button(root, text="^2", padx=36, pady=20, command=squarenumber, fg = "Blue")

buttonmultiply = Button(root, text="x", padx=40, pady=20, command=numbermultiply)
buttonsubtract = Button(root, text="-", padx=40, pady=20, command=numbersubtract)
buttonadd = Button(root, text="+", padx=39, pady=20, command=numberadd)
buttonequals = Button(root, text="=", padx=39, pady=20, command=numbercalc)

buttonclear = Button(root, text="clear", padx= 30, pady=20, command=clearinput, fg = "#fc8c03")
buttondelete = Button(root, text="delete", padx=27, pady=20, command=deleteinput, fg = "#fc8c03")
buttonexit = Button(root, text="exit", padx=34, pady=20, command=closeapp, fg = "Red")
buttondivide = Button(root, text="/", padx=40, pady=20, command=numberdivide)

buttonsqrt = Button(root, text="sqrt", padx=32, pady=20, command=sqrtnumber, fg = "Blue")
blank1 = Label(root, padx=40, pady=20)
blank2 = Label(root, padx=40, pady=20)

ansbutton = Button(root, text="ans", padx=34, pady=20, command=ansinput, fg = "Blue")

colourbutton = Button(root, text="colour", padx=26, pady=20, command=colourchange, fg = "Purple")

pibutton = Button(root, text="π", padx=40, pady=20, command = lambda: piinput())

#displaying on screen

ansbutton.grid(row = 3, column = 1)

buttonsqrt.grid(row = 3, column = 0)
blank1.grid(row = 3, column = 1)
buttondivide.grid(row = 3, column = 3)
buttonsquare.grid(row = 3, column = 2)

buttonclear.grid(row = 2, column = 0)
buttondelete.grid(row = 2, column = 1)
buttonexit.grid(row = 2, column = 2)

button1.grid(row = 6, column = 0)
button2.grid(row = 6, column = 1)
button3.grid(row = 6, column = 2)

button4.grid(row = 5, column = 0)
button5.grid(row = 5, column = 1)
button6.grid(row = 5, column = 2)

button7.grid(row = 4, column = 0)
button8.grid(row = 4, column = 1)
button9.grid(row = 4, column = 2)

button0.grid(row = 7, column = 0)
buttondecpoint.grid(row = 7, column = 1)
# blank2.grid(row = 7, column = 2)

buttonmultiply.grid(row = 4, column = 3)
buttonsubtract.grid(row = 5, column = 3)
buttonadd.grid(row = 6, column = 3)
buttonequals.grid(row = 7, column = 3)

pibutton.grid(row = 7, column = 2)



print("opened")
root.mainloop()
print("closed")

