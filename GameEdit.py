import tkinter as tk
import random
count = 0
points = 0
#chances = 3

top = tk.Tk()
#top.config(bg = 'orange') #to change background color
top.title("Word Game")
top.geometry("250x300")
#word list contains words with either whole string capitel letters or small
wordslist = ["COMPUTER",'LAPTOP','PHONE','television']

def changecase():
    global count#count to change case
    if(count%2==1):
        c1=c2=0
        c3=2#to increment column counts
        #upper case keys on keyboard
        aboveline='QWERTYUIOP'
        middleline = 'ASDFGHJKL'
        lowline='ZXCVBNM'
        for letter in aboveline:
            letter = tk.Button(top, text = letter, command = lambda i=letter : settext(i)).grid(row=5,column=c1)
            #grid to set up button in specefied position
            c1+=1#column increment
        for i in middleline:
            i=tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=6,column=c2)
            c2+=1
        for i in lowline:
            i = tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=7,column=c3)
            c3+=1
        count+=1#count increment to change case
    else:
       # global count already declared in function
        c1=c2=0
        c3=2
        #lower case keys on keyboard
        aboveline='qwertyuiop'
        middleline = 'asdfghjkl'
        lowline='zxcvbnm'
        for letter in aboveline:
            letter = tk.Button(top, text = letter, command = lambda i=letter : settext(i)).grid(row=5,column=c1)
            c1+=1#column increment
        for i in middleline:
            i=tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=6,column=c2)
            c2+=1
        for i in lowline:
            i = tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=7,column=c3)
            c3+=1
        count+=1#count increment to change case

def getword():
    word = random.choice(wordslist) #Randomly choosing words from list 
    missing_text = ''
    #words in ourlist will be of length >=4
    if(len(word)==5 or len(word)==4):#words of length <= 5
        first = random.randint(0,3)#position of first word to be displayed
        second = random.randint(0,3)#position of second word to be displayed
        for i in range(len(word)):
            if(i==first or i==second):
                missing_text += word[i]
            else:
                missing_text += ' _'
    elif(len(word)>5):#words of length >5
        first = random.randint(0,2)
        second = random.randint(3,6)
        third = random.randint(7,9)
        #positions of words to be displayed on Label
        for i in range(len(word)):
            if(i==first or i==second or i==third):
                missing_text += word[i]
            else:
                missing_text += ' _'
    return(missing_text)
  
def settext(char):#functions to insert characters on Entry
    l = len(e1.get())
    e1.insert(l,char)

def backspace():#function for backspace
    txt=e1.get()
    e1.delete(0,tk.END)
    e1.insert(0,txt[:-1])

def resettext():#function to remove whole text entered on entry
    e1.delete(0,tk.END)
   
def evaluate():#function to evaluate if entered word is in list or not
    global points
    while(True):
        text = e1.get()
        if(text in wordslist):#if text entered by user is in list
            points += 10
            pts.insert(0,str(points))
            result_msg = tk.Message(top,text="YOUR ARE CORRECT:)",width=100).grid(row=8,column=0,columnspan=10)
            break
        else:#if text entered by user not in list
            e1.delete(0,tk.END)
            result_msg = tk.Message(top,text="TRY AGAIN!",width=100).grid(row=8,column=0,columnspan=10)
            break
    
title = tk.Label(top, text = "WORD GAME")#title display
title.grid(row=0,column=0,columnspan=10)

l1 = tk.Label(top, text = "Guess the word")#label : guess the word
l1.grid(row=1,column=0,columnspan =4)

def textCalling():#displaying word on an label
    l2 = tk.Label(top, text = getword() )
    l2.grid(row=1,column=4,columnspan=6)
textCalling()

l3 = tk.Label(top, text ='Enter your guess' )#label : enter your guess
l3.grid(row=2,column=0,columnspan=4)

e1 = tk.Entry(top, bd = 10)#entry to enter user response
e1.grid(row=2,column=4,columnspan=6)

#initially setting up keyboard with lower case
changecase()

b_ = tk.Button(top, text = "<-", command = lambda: backspace()).grid(row=6,column=9)#backspace button
#shift button to change case
shift = tk.Button(top, text = "shift", command = lambda : changecase(), width=5).grid(row=7,column=0,columnspan=2)
enter = tk.Button(top, text = "<-|", command = lambda : evaluate()).grid(row=7,column=9) #enter button


def nextWord():#function to get next word
    clrlabel = tk.Label(top, text = "                                      " )#blank label to repaint a new word on it
    clrlabel.grid(row=1,column=4,columnspan=6)
    textCalling()#getting a label with word on it
    resettext()#reset entry to enter new response
    #blank label to repaint a new note on the previous one
    result_msg = tk.Message(top,text="                                      ",width=100).grid(row=8,column=0,columnspan=10)

nxt = tk.Button(top,text = "next", command = lambda : nextWord()).grid(row = 9,column = 0, columnspan = 4)#next button
points_label = tk.Label(top,text="points").grid(row=9,column=3,columnspan=3)#points label
pts = tk.Entry(top,width=2)#entry to display points
pts.grid(row=9,column=6)#grid() to place entry in specefied position

reset = tk.Button(top,text="reset", command = lambda : resettext()).grid(row=9,column=8,columnspan=4)#reset button
note = tk.Label(top, text = "Press X to quit the game").grid(row = 10, column = 1, columnspan = 9)#label
note2 = tk.Label(top, text = "Enter response by seeing given word:)").grid(row = 11, column = 1, columnspan = 9)#label
top.mainloop()