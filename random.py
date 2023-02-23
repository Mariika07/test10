from tkinter import*
from random import*
root=Tk()
root.geometry('800x600')
root.resizable(False,False)
def button_1():
    canvas.delete('all')
    a=randint(0,2)
    if a==0:
        canvas.create_oval(20,20,150,150)   
    if a==1:
        canvas.create_rectangle(20,20,150,150)
    if a==2:
       canvas.create_polygon(20,20,150,200,250,150, fill='white',outline='black')
canvas=Canvas(root, width=300, height=300, bg='white')
canvas.pack()
Button(root,text='Нажми',width=15, height=3,bg='gray',command=button_1).pack()
root.mainloop()