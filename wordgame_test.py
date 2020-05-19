# -*- coding: utf-8 -*-
"""
Created on Thu Jan  2 20:26:06 2020

@author: Pavan Kalyan
"""

import tkinter as tk
import random
count = 0
points = 0
chances = 3

top = tk.Tk()
top.title("Word Game")
top.geometry("250x300")
#word = 'GEO'
wordslist = ["COMPUTER",'LAPTOP']

def changecase():
    global count
   
    if(count%2==0):
        c1=c2=0
        c3=2
        aboveline='QWERTYUIOP'
        middleline = 'ASDFGHJKL'
        lowline='ZXCVBNM'
        for letter in aboveline:
            letter = tk.Button(top, text = letter, command = lambda i=letter : settext(i)).grid(row=5,column=c1)
            c1+=1
        for i in middleline:
            i=tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=6,column=c2)
            c2+=1
        for i in lowline:
            i = tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=7,column=c3)
            c3+=1
            
        count+=1
    else:
       # global count already declared in function
        c1=c2=0
        c3=2
        aboveline='qwertyuiop'
        middleline = 'asdfgjhkl'
        lowline='zxcvbnm'
        for letter in aboveline:
            letter = tk.Button(top, text = letter, command = lambda i=letter : settext(i)).grid(row=5,column=c1)
            c1+=1
        for i in middleline:
            i=tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=6,column=c2)
            c2+=1
        for i in lowline:
            i = tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=7,column=c3)
            c3+=1
        count+=1
def getword():
    word = random.choice(wordslist)  
    missing_text = ''
    if(len(word)<5):
        first = random.randint(0,4)
        second = random.randint(0,4)
        for i in range(len(word)):
            if(i==first or i==second):
                missing_text += word[i]
            else:
                missing_text += '_'
    elif(len(word)>5):
        first = random.randint(0,2)
        second = random.randint(3,6)
        third = random.randint(7,9)
        for i in range(len(word)):
            if(i==first or i==second or i==third):
                missing_text += word[i]
            else:
                missing_text += '_'
    return(missing_text)
    
def settext(char):
    l = len(e1.get())
    e1.insert(l,char)

def backspace():
    txt=e1.get()
    e1.delete(0,tk.END)
    e1.insert(0,txt[:-1])

def resettext():
    e1.delete(0,tk.END)


    
def evaluate():
    global points
    global chances
    while(chances>0):
        text = e1.get()
        if(text in wordslist):
            points += 10
            pts.insert(0,str(points))
            result_msg = tk.Message(top,text="YOUR ARE CORRECT:)",width=100).grid(row=8,column=0,columnspan=10)
            break
        else:
            if(chances>0):
                chances -=1
                e1.delete(0,tk.END)
                ch.insert(0,str(chances))
                result_msg = tk.Message(top,text="TRY AGAIN!",width=100).grid(row=8,column=0,columnspan=10)
   #if(chances<=0):
            else:
                result_msg = tk.Message(top,text="YOU LOSE!").grid(row=8,column=0,columnspan=10)
                chances = 3
    
title = tk.Label(top, text = "WORD GAME")
title.grid(row=0,column=0,columnspan=10)

l1 = tk.Label(top, text = "Guess the word")
l1.grid(row=1,column=0,columnspan =4)

l2 = tk.Label(top, text = getword() )
l2.grid(row=1,column=4,columnspan=6)

l3 = tk.Label(top, text ='enter your guess' )
l3.grid(row=2,column=0,columnspan=4)

e1 = tk.Entry(top, bd = 10)
e1.grid(row=2,column=4,columnspan=6)

c1=c2=0
c3=2
aboveline='qwertyuiop'
middleline = 'asdfghjkl'
lowline='zxcvbnm'
for letter in aboveline:
    letter = tk.Button(top, text = letter, command = lambda i=letter : settext(i)).grid(row=5,column=c1)
    c1+=1
for i in middleline:
    i=tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=6,column=c2)
    c2+=1
for i in lowline:
    i = tk.Button(top, text = i, command = lambda x=i: settext(x)).grid(row=7,column=c3)
    c3+=1


b_ = tk.Button(top, text = "<-", command = lambda: backspace()).grid(row=6,column=9)
shift = tk.Button(top, text = "shift", command = lambda : changecase(), width=5).grid(row=7,column=0,columnspan=2)
enter = tk.Button(top, text = "<-|", command = lambda : evaluate()).grid(row=7,column=9)

chances_label = tk.Label(top,text="chances").grid(row=9,column=0,columnspan=2)
ch = tk.Entry(top,width=2)
ch.grid(row=9,column=2)
points_button = tk.Label(top,text="points").grid(row=9,column=3,columnspan=3)
pts = tk.Entry(top,width=2)
pts.grid(row=9,column=6)

reset = tk.Button(top,text="reset", command = lambda : resettext()).grid(row=9,column=8,columnspan=4)
top.mainloop()