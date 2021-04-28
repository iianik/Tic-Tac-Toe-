#Dey Anik
#17-33933-1


from tkinter import *
from tkinter import messagebox
import random as r



def button(frame):         
    b=Button(frame,padx=1,bg="White",width=3,text="   ",font=('arial',60,'bold'))
    return b

def change_a():             
    global a
    for i in ['O','X']:
        if not(i==a):
            a=i
            break


def reset():                
    global a
    for i in range(3):
        for j in range(3):
                b[i][j]["text"]=" "
                b[i][j]["state"]=NORMAL
    a=r.choice(['O','X'])


def check():                
    for i in range(3):
            if(b[i][0]["text"]==b[i][1]["text"]==b[i][2]["text"]==a or b[0][i]["text"]==b[1][i]["text"]==b[2][i]["text"]==a):
                    messagebox.showinfo("Player!!","'"+a+"'Player has won")
                    reset()

    if(b[0][0]["text"]==b[1][1]["text"]==b[2][2]["text"]==a or b[0][2]["text"]==b[1][1]["text"]==b[2][0]["text"]==a):
        messagebox.showinfo("Player!!","'"+a+"' Player has won")
        reset()   

    elif(b[0][0]["state"]==b[0][1]["state"]==b[0][2]["state"]==b[1][0]["state"]==b[1][1]["state"]==b[1][2]["state"]==b[2][0]["state"]==b[2][1]["state"]==b[2][2]["state"]==DISABLED):
        messagebox.showinfo("Tied!!","Bad luck the match ended in a draw")
        reset()

def click(row,col):
        b[row][col].config(text=a,state=DISABLED,disabledforeground=colour[a])
        check()
        change_a()
       

root=Tk()                  
root.title("Tic-Tac-Toe")   
a=r.choice(['O','X'])       
colour={'O':"black",'X':"red"}
b=[[],[],[]]
for i in range(3):
        for j in range(3):
                b[i].append(button(root))
                b[i][j].config(command= lambda row=i,col=j:click(row,col))
                b[i][j].grid(row=i,column=j)

root.mainloop()




#Dey Anik
#17-33933-1