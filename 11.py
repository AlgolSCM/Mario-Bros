from tkinter import *
w = Tk()
img=PhotoImage(file='mision.gif')
img2=PhotoImage(file='mision.gif')
def a():
    
    Bo3= Button(w,image=img,height=53,width=40,command =b).place(x=80,y=50)
    Bo4= Button(w,image=img2,height=53,width=40,command =d).place(x=210,y=50)
   
    lblmision1=Label(text='Herramienta roja',font=('Book Antiqua',8)).place(x=50,y=130)
    lblmision2=Label(text='Herramienta azul',font=('Book Antiqua',8)).place(x=170,y=130)
def b():
    print('en mision1')
    
def d():
      print('en mision2')   
w.geometry('300x180')
w.title("Aliados")
Bo = Button(w,text="Acciones de Aliados",command = a).place(x=100,y=10)


w.mainloop()              
                
