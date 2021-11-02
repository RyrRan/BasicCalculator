from tkinter import *
from PIL import ImageTk, Image, ImageOps


root = Tk()
root.title("Calculator")
root.iconbitmap('calculatorIcon.ico')


inputBox = Entry(root, width=50, borderwidth=5)
inputBox.grid(row=0,column=0,columnspan=3,padx=5,pady=5)

currentTotal = 0
isSummed = False
lastOperation = ''
firstNum = 0
incomingNum = 0

def button_click(number):
    global isSummed
    if (number >= 0 and number <= 9 and isSummed == False):
        currentValue = inputBox.get()
        currentValue = str(currentValue) + str(number)
        inputBox.delete(0, END)
        inputBox.insert(0, currentValue)


def compute_clear():
    global isSummed
    global currentTotal
    global lastOperation
    global firstNum 
    global incomingNum
    firstNum = 0
    incomingNum = 0
    lastOperation = ''
    currentTotal = 0
    isSummed = False
    inputBox.delete(0,END)

def compute(whichOp):
    global firstNum 
    global incomingNum
    global lastOperation
    global currentTotal
    if(lastOperation == '' and isSummed == False):
        firstNum = int(inputBox.get())
        currentTotal = firstNum
    elif(lastOperation != '' and isSummed == False):
        if(lastOperation == '+'):
            incomingNum = int(inputBox.get())
            currentTotal = int(firstNum) + int(incomingNum)
        elif(lastOperation == '-'):
            incomingNum = int(inputBox.get())
            currentTotal = int(firstNum) - int(incomingNum)
        elif(lastOperation == '*'):
            incomingNum = int(inputBox.get())
            currentTotal = int(firstNum) * int(incomingNum)
        elif(lastOperation == '/'):
            incomingNum = int(inputBox.get())
            currentTotal = float(firstNum) / float(incomingNum)
        firstNum = currentTotal
    lastOperation = whichOp
    inputBox.delete(0,END)

def compute_equal(lastOp):
    global currentTotal
    global isSummed
    global firstNum
    global lastOperation
    if(inputBox.get() != None and isSummed == False and lastOp == '+'):
        currentTotal = int(currentTotal) + int(inputBox.get())
    elif(inputBox.get() != None and isSummed == False and lastOp == '-'):
        currentTotal = int(currentTotal) - int(inputBox.get())
    elif(inputBox.get() != None and isSummed == False and lastOp == '*'):
        currentTotal = int(currentTotal) * int(inputBox.get())
    elif(inputBox.get() != None and isSummed == False and lastOp == '/'):
        currentTotal = float(currentTotal) / float(inputBox.get())
    if(isSummed == False):    
        print(currentTotal)
        inputBox.delete(0,END)
        inputBox.insert(0, str(currentTotal))
        currentTotal = int(inputBox.get())
        inputBox.delete(0,END)
        inputBox.insert(0,"Total: " + str(currentTotal))
        isSummed = True



button9 = Button(root,width=10,height=5, text="9",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(9))
button8 = Button(root,width=10,height=5, text="8",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(8)) 
button7 = Button(root,width=10,height=5, text="7",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(7)) 
button6 = Button(root,width=10,height=5, text="6",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(6)) 
button5 = Button(root,width=10,height=5, text="5",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(5)) 
button4 = Button(root,width=10,height=5, text="4",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(4)) 
button3 = Button(root,width=10,height=5, text="3",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(3)) 
button2 = Button(root,width=10,height=5, text="2",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(2)) 
button1 = Button(root,width=10,height=5, text="1",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(1)) 
button0 = Button(root,width=10,height=5, text="0",padx=25,pady=25, fg="blue", bg="grey", command=lambda:button_click(0)) 
buttonAdd = Button(root,width=10,height=5, text="+",padx=25,pady=25, fg="black", bg="royalblue", command=lambda:compute('+'))
buttonEqual = Button(root,width=10,height=5, text="=",padx=25,pady=25, fg="blue", bg="peachpuff", command=lambda:compute_equal(lastOperation))
buttonSubtract = Button(root,width=10,height=5, text="-",padx=25,pady=25, fg="black", bg="royalblue", command=lambda:compute('-'))
buttonMultiply = Button(root,width=10,height=5, text="x",padx=25,pady=25, fg="black", bg="royalblue", command=lambda:compute('*')) 
buttonDivide = Button(root,width=10,height=5, text="/",padx=25,pady=25, fg="black", bg="royalblue", command=lambda:compute('/'))
buttonClear = Button(root,width=47,height=5, text="Clear",padx=25,pady=25, fg="white", bg="darkred", command=compute_clear)



button9.grid(row=1, column=0)
button8.grid(row=1, column=1)
button7.grid(row=1, column=2)
button6.grid(row=2, column=0)
button5.grid(row=2, column=1)
button4.grid(row=2, column=2)
button3.grid(row=3, column=0)
button2.grid(row=3, column=1)
button1.grid(row=3, column=2)
button0.grid(row=4, column=0)
buttonAdd.grid(row=4, column=1)
buttonSubtract.grid(row=4, column=2)
buttonMultiply.grid(row=5, column=0)
buttonDivide.grid(row=5, column=1)
buttonEqual.grid(row=5, column=2)
buttonClear.grid(row=6, column=0, columnspan=3)


root.mainloop()
