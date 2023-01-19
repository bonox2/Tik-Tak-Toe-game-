#Tik tak toe game
#Tik Tak toe game
#Jan 27 2021
#Illia Goncharov
import random
from tkinter import*
from tkinter.ttk import *
from tkinter import messagebox

window = Tk()
window.title('Test program')
window.geometry('350x260')

# photos
blank = PhotoImage(file="blank.png")
imgX = PhotoImage(file="imgX.png")
imgO = PhotoImage(file="imgO.png")
imgXWin = PhotoImage(file="imgXWin.png")
imgOWin = PhotoImage(file="imgOWin.png")
# photos
# veriables
bot = False
tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
xTurn = True
moves = 0

# veriables

#single player mode all posibilites

def botMode():
    global bot, xTurn, tttSquares, moves
    if bot == False:
        btnBot.configure(text='Single Player ON')
        btn0.configure(command=lambda: ai(btn0))
        btn1.configure(command=lambda: ai(btn1))
        btn2.configure(command=lambda: ai(btn2))
        btn3.configure(command=lambda: ai(btn3))
        btn4.configure(command=lambda: ai(btn4))
        btn5.configure(command=lambda: ai(btn5))
        btn6.configure(command=lambda: ai(btn6))
        btn7.configure(command=lambda: ai(btn7))
        btn8.configure(command=lambda: ai(btn8))
        btn0.configure(image=blank, state='')
        btn1.configure(image=blank, state='')
        btn2.configure(image=blank, state='')
        btn3.configure(image=blank, state='')
        btn4.configure(image=blank, state='')
        btn5.configure(image=blank, state='')
        btn6.configure(image=blank, state='')
        btn7.configure(image=blank, state='')
        btn8.configure(image=blank, state='')
        tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        xTurn = True
        moves = 0
        bot = True
    else:
        btnBot.configure(text='Single Player OFF')
        btn0.configure(command=lambda: clicked(btn0))
        btn1.configure(command=lambda: clicked(btn1))
        btn2.configure(command=lambda: clicked(btn2))
        btn3.configure(command=lambda: clicked(btn3))
        btn4.configure(command=lambda: clicked(btn4))
        btn5.configure(command=lambda: clicked(btn5))
        btn6.configure(command=lambda: clicked(btn6))
        btn7.configure(command=lambda: clicked(btn7))
        btn8.configure(command=lambda: clicked(btn8))
        btn0.configure(image=blank, state='')
        btn1.configure(image=blank, state='')
        btn2.configure(image=blank, state='')
        btn3.configure(image=blank, state='')
        btn4.configure(image=blank, state='')
        btn5.configure(image=blank, state='')
        btn6.configure(image=blank, state='')
        btn7.configure(image=blank, state='')
        btn8.configure(image=blank, state='')
        tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        xTurn = True
        moves = 0
        bot = False

#function to cancel 2 players mode code
def ai(buttons):
    global xTurn, moves, tttSquares
    moves+=1
    if xTurn == True:
        buttons.configure(image=imgX, state=DISABLED)
        if buttons == btn0:
            tttSquares[0] = 1
        elif buttons == btn1:
            tttSquares[1] = 1
        elif buttons == btn2:
            tttSquares[2] = 1
        elif buttons == btn3:
            tttSquares[3] = 1
        elif buttons == btn4:
            tttSquares[4] = 1
        elif buttons == btn5:
            tttSquares[5] = 1
        elif buttons == btn6:
            tttSquares[6] = 1
        elif buttons == btn7:
            tttSquares[7] = 1
        elif buttons == btn8:
            tttSquares[8] = 1
        checkWin()



    rNumber=random.randint(0,8)
    while tttSquares[rNumber]!=0:
        rNumber=random.randint(0,8)
    if rNumber==0:
        tttSquares[0] = 2
        btn0.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==1:
        tttSquares[1] = 2
        btn1.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==2:
        tttSquares[2] = 2
        btn2.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==3:
        tttSquares[3] = 2
        btn3.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==4:
        tttSquares[4] = 2
        btn4.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==5:
        tttSquares[5] = 2
        btn5.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==6:
        tttSquares[6] = 2
        btn6.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==7:
        tttSquares[7] = 2
        btn7.configure(image=imgO, state=DISABLED)
        moves+=1
    elif rNumber==8:
        tttSquares[8] = 2
        btn8.configure(image=imgO, state=DISABLED)
        moves+=1
    checkWin()




#button to change mode
btnBot = Button(window, text='Single Player OFF', command=botMode)
btnBot.grid(column=4, row=1)



#code to 2 players mode
def clicked(buttons):
    global xTurn, moves, tttSquares
    moves += 1
    if xTurn == True:
        buttons.configure(image=imgX, state=DISABLED)
        if buttons == btn0:
            tttSquares[0] = 1
        elif buttons == btn1:
            tttSquares[1] = 1
        elif buttons == btn2:
            tttSquares[2] = 1
        elif buttons == btn3:
            tttSquares[3] = 1
        elif buttons == btn4:
            tttSquares[4] = 1
        elif buttons == btn5:
            tttSquares[5] = 1
        elif buttons == btn6:
            tttSquares[6] = 1
        elif buttons == btn7:
            tttSquares[7] = 1
        elif buttons == btn8:
            tttSquares[8] = 1
        xTurn = False
        checkWin()
    else:
        buttons.configure(image=imgO, state=DISABLED)
        if buttons == btn0:
            tttSquares[0] = 2
        elif buttons == btn1:
            tttSquares[1] = 2
        elif buttons == btn2:
            tttSquares[2] = 2
        elif buttons == btn3:
            tttSquares[3] = 2
        elif buttons == btn4:
            tttSquares[4] = 2
        elif buttons == btn5:
            tttSquares[5] = 2
        elif buttons == btn6:
            tttSquares[6] = 2
        elif buttons == btn7:
            tttSquares[7] = 2
        elif buttons == btn8:
            tttSquares[8] = 2
        xTurn = True
        checkWin()
        #check win X
def checkWin():
    global tttSquares,xTurn,moves
    if (tttSquares[0] == tttSquares[1] == tttSquares[2] == 1) or (tttSquares[3] == tttSquares[4] == tttSquares[5] == 1) or (tttSquares[6] == tttSquares[7] == tttSquares[8] == 1) or (tttSquares[0] == tttSquares[3] == tttSquares[6] == 1) or (tttSquares[1] == tttSquares[4] == tttSquares[7] == 1) or (tttSquares[2] == tttSquares[5] == tttSquares[8] == 1) or (tttSquares[0] == tttSquares[4] == tttSquares[8] == 1) or (tttSquares[2] == tttSquares[4] == tttSquares[6] == 1):
        if (tttSquares[0] == tttSquares[1] == tttSquares[2] == 1):
            btn0.configure(image=imgXWin)
            btn1.configure(image=imgXWin)
            btn2.configure(image=imgXWin)
        elif (tttSquares[3] == tttSquares[4] == tttSquares[5] == 1):
            btn3.configure(image=imgXWin)
            btn4.configure(image=imgXWin)
            btn5.configure(image=imgXWin)
        elif (tttSquares[6] == tttSquares[7] == tttSquares[8] == 1):
            btn6.configure(image=imgXWin)
            btn7.configure(image=imgXWin)
            btn8.configure(image=imgXWin)
        elif (tttSquares[0] == tttSquares[3] == tttSquares[6] == 1):
            btn0.configure(image=imgXWin)
            btn3.configure(image=imgXWin)
            btn6.configure(image=imgXWin)
        elif (tttSquares[1] == tttSquares[4] == tttSquares[7] == 1):
            btn1.configure(image=imgXWin)
            btn4.configure(image=imgXWin)
            btn7.configure(image=imgXWin)
        elif (tttSquares[2] == tttSquares[5] == tttSquares[8] == 1):
            btn2.configure(image=imgXWin)
            btn5.configure(image=imgXWin)
            btn8.configure(image=imgXWin)
        elif (tttSquares[0] == tttSquares[4] == tttSquares[8] == 1):
            btn0.configure(image=imgXWin)
            btn4.configure(image=imgXWin)
            btn8.configure(image=imgXWin)
        elif (tttSquares[2] == tttSquares[4] == tttSquares[6] == 1):
            btn2.configure(image=imgXWin)
            btn4.configure(image=imgXWin)
            btn6.configure(image=imgXWin)
        messagebox.showinfo('X Wins')
        btn0.configure(image=blank, state='')
        btn1.configure(image=blank, state='')
        btn2.configure(image=blank, state='')
        btn3.configure(image=blank, state='')
        btn4.configure(image=blank, state='')
        btn5.configure(image=blank, state='')
        btn6.configure(image=blank, state='')
        btn7.configure(image=blank, state='')
        btn8.configure(image=blank, state='')
        tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        xTurn = True
        moves = 0
        #check win O
    elif (tttSquares[0] == tttSquares[1] == tttSquares[2] == 2) or (tttSquares[3] == tttSquares[4] == tttSquares[5] == 2) or (tttSquares[6] == tttSquares[7] == tttSquares[8] == 2) or (tttSquares[0] == tttSquares[3] == tttSquares[6] == 2) or (tttSquares[1] == tttSquares[4] == tttSquares[7] == 2) or (tttSquares[2] == tttSquares[5] == tttSquares[8] == 2) or (tttSquares[0] == tttSquares[4] == tttSquares[8] == 2) or (tttSquares[2] == tttSquares[4] == tttSquares[6] == 2):
        if (tttSquares[0] == tttSquares[1] == tttSquares[2] == 2):
            btn0.configure(image=imgOWin)
            btn1.configure(image=imgOWin)
            btn2.configure(image=imgOWin)
        elif (tttSquares[3] == tttSquares[4] == tttSquares[5] == 2):
            btn3.configure(image=imgOWin)
            btn4.configure(image=imgOWin)
            btn5.configure(image=imgOWin)
        elif (tttSquares[6] == tttSquares[7] == tttSquares[8] == 2):
            btn6.configure(image=imgOWin)
            btn7.configure(image=imgOWin)
            btn8.configure(image=imgOWin)
        elif (tttSquares[0] == tttSquares[3] == tttSquares[6] == 2):
            btn0.configure(image=imgOWin)
            btn3.configure(image=imgOWin)
            btn6.configure(image=imgOWin)
        elif (tttSquares[1] == tttSquares[4] == tttSquares[7] == 2):
            btn1.configure(image=imgOWin)
            btn4.configure(image=imgOWin)
            btn7.configure(image=imgOWin)
        elif (tttSquares[2] == tttSquares[5] == tttSquares[8] == 2):
            btn2.configure(image=imgOWin)
            btn5.configure(image=imgOWin)
            btn8.configure(image=imgOWin)
        elif (tttSquares[0] == tttSquares[4] == tttSquares[8] == 2):
            btn0.configure(image=imgOWin)
            btn4.configure(image=imgOWin)
            btn8.configure(image=imgOWin)
        elif (tttSquares[2] == tttSquares[4] == tttSquares[6] == 2):
            btn2.configure(image=imgOWin)
            btn4.configure(image=imgOWin)
            btn6.configure(image=imgOWin)
        messagebox.showinfo('O Wins')
        btn0.configure(image=blank, state='')
        btn1.configure(image=blank, state='')
        btn2.configure(image=blank, state='')
        btn3.configure(image=blank, state='')
        btn4.configure(image=blank, state='')
        btn5.configure(image=blank, state='')
        btn6.configure(image=blank, state='')
        btn7.configure(image=blank, state='')
        btn8.configure(image=blank, state='')
        tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        xTurn = True
        moves = 0
        #Check tie
    elif moves == 9:
        messagebox.showinfo('Its Tie')
        btn0.configure(image=blank, state='')
        btn1.configure(image=blank, state='')
        btn2.configure(image=blank, state='')
        btn3.configure(image=blank, state='')
        btn4.configure(image=blank, state='')
        btn5.configure(image=blank, state='')
        btn6.configure(image=blank, state='')
        btn7.configure(image=blank, state='')
        btn8.configure(image=blank, state='')
        tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        xTurn = True
        moves = 0


def reset():
    global tttSquares,xTurn,moves
    btn0.configure(image=blank, state='')
    btn1.configure(image=blank, state='')
    btn2.configure(image=blank, state='')
    btn3.configure(image=blank, state='')
    btn4.configure(image=blank, state='')
    btn5.configure(image=blank, state='')
    btn6.configure(image=blank, state='')
    btn7.configure(image=blank, state='')
    btn8.configure(image=blank, state='')
    tttSquares = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    xTurn = True
    moves = 0




btnReset = Button(window, text='Reset', command=reset)
btnReset.grid(column=4, row=0)

# top btns
btn0 = Button(window, image=blank,state='', command=lambda: clicked(btn0))
btn0.grid(row=0, column=0)

btn1 = Button(window, image=blank,state='', command=lambda: clicked(btn1))
btn1.grid(row=0, column=1)

btn2 = Button(window, image=blank,state='', command=lambda: clicked(btn2))
btn2.grid(row=0, column=2)
# top btns
# mid buttons
btn3 = Button(window, image=blank,state='', command=lambda: clicked(btn3))
btn3.grid(column=0, row=1)

btn4 = Button(window, image=blank,state='', command=lambda: clicked(btn4))
btn4.grid(column=1, row=1)

btn5 = Button(window, image=blank,state='', command=lambda: clicked(btn5))
btn5.grid(column=2, row=1)
# mid buttons
# bot buttons
btn6 = Button(window, image=blank,state='', command=lambda: clicked(btn6))
btn6.grid(column=0, row=2)

btn7 = Button(window, image=blank,state='', command=lambda: clicked(btn7))
btn7.grid(column=1, row=2)

btn8 = Button(window, image=blank,state='', command=lambda: clicked(btn8))
btn8.grid(column=2, row=2)
# bot buttons


window.mainloop()
