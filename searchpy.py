import mysql.connector
from tkinter import *
from tkinter import messagebox

def search():
    try:
        mydb=mysql.connector.connect(user='root',password='parmar',\
                            host='localhost',database='collage_stu')
        print(mydb)
        cur=mydb.cursor()
        sql="select * from student where rollno='%s'"%rollno.get()
        cur.execute(sql)
        result=cur.fetchone()
        name.set(result[1])
        age.set(result[2])
        e1.configure(state='disabled')
        mydb.close()
    except:
        messagebox.showinfo('No Data','No such data avalilable...')
        clear()


def clear():
    rollno.set('')
    name.set('')
    age.set('')
    e1.configure(state='normal')

w1=Tk()
w1.title('my App')
w1.geometry('500x200')
ptitle=Label(w1,text='''program to search students details from the student table''')
ptitle.grid(row=0,column=0,columnspan=2)

rollno=StringVar()
name=StringVar()
age=StringVar()

l1=Label(w1,text='RollNo')
e1=Entry(w1,textvariable=rollno)

l2=Label(w1,text='Name')
e2=Entry(w1,textvariable=name)

l3=Label(w1,text='Age')
e3=Entry(w1,textvariable=age)

b1=Button(w1,text='Search',command=search)
b2=Button(w1,text='Clear',command=clear)

l1.grid(row=1,column=0)
e1.grid(row=1,column=1)
l2.grid(row=2,column=0)
e2.grid(row=2,column=1)
l3.grid(row=3,column=0)
e3.grid(row=3,column=1)
b1.grid(row=1,column=2)
b2.grid(row=4,column=0)
w1.mainloop()


















