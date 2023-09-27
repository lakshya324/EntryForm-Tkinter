#by Lakshya 575 words 7,255 characters 272 lines (Last Update: 23 dec 2021 At 16:14)
from tkinter import *
from tkinter.filedialog import *
import tkinter.messagebox as tm
import tkinter.font 
import json
import time
import os

root=Tk()

root.geometry("480x640")
root.maxsize(480,640)
root.maxsize(480,640)

root.title("Enter Entries -by Lakshya")

root.config(bg="orange")

f=tkinter.font.Font( family ="Times", size = 50,  weight ="bold",underline =1)
Label(root,text="Entries Form",font=f,bg="orange",fg="blue").pack(padx=10,pady=15,fill="x")

Label(root,text="",bg="orange").pack(padx=10,pady=30,fill="x")

f1=tkinter.font.Font( size = 25,  weight ="bold")


me=StringVar()
me.set("")
Label(root,textvariable=me,bg="orange",fg="red",font=f1).pack(side=BOTTOM,padx=10,pady=10,fill="x")


fsl=r"F:\Coding\python\Run-WorkShop\Completed-Projects\Entry Form_by-Lakshya\File_Path.txt"
fr=open(fsl,"rt")
file =fr.read()
fr.close()

#fsl="File Location.txt"
# fr=open("File Location.txt","rt")
# file =fr.read()
# fr.close()

def fo():
    global file , me
    if file==None or file=="":
        fo2()
    else:
        a=tm.askyesno("Warning",f"You Current File Loction is '{file}'\nDo you want to Change?")
        if a==True:
            fo2()
        else:
            pass

def fo2():
    file=askopenfilename(defaultextension="*.txt",filetype=[("Text File","*.txt")])
    if file==None or file=="":
        tm.showerror("Error Occured","File not found")
    else:
        fs=open(fsl,"wt")
        fs.write(file)
        fs.close()
        me.set("File Path Saved")
        root.update()
        time.sleep(3)
        me.set("")
        root.update()


def fpath():
    if file==None or file=="":
        a=tm.askyesno("File Location","No File Location Found...\nCkeck 'Yes' to select a location ")
        if a==True:
            fo2()
    else:
        tm.showinfo("File Location",f"File Location is:\n'{file}'")



m=Menu(root)
m1=Menu(root,tearoff=0)
m2=Menu(root,tearoff=0)


m1.add_command(label="Change Path",command=fo)
m1.add_command(label="File Location",command=fpath)
m1.add_separator()
m1.add_command(label="Exit",command=root.destroy)


m2.add_command(label="About Us")
m2.add_separator()
m2.add_command(label="Contact Us")


m.add_cascade(label="File",menu=m1)
m.add_cascade(label="Help",menu=m2)

root.config(menu=m)



pass2= False
def af():
    global pass2 , file
    fr=open(fsl,"rt")
    file =fr.read()
    fr.close()
    if file==None or file=="":
        tm.showerror("Error","File not found")
        a=tm.askyesno("File Location","Ckeck 'Yes' to select a location...")
        if a==True:
            fo2()
    else:
        pass2=True
        for i in root.winfo_children():
            i.destroy()
        a=StringVar()
        a.set("Loading")
        Label(root,textvariable=a,font=f1,bg="orange",fg="blue").pack(expand=TRUE)

        for i in range(5):
            for j in range(1,4):
                a.set("Loading"+"."*j)
                root.update()
                time.sleep(0.1)

        for i in range(101):
            if i==0:
                a.set("Scanning File...")
                root.update()
                time.sleep(0.25)
            elif i==100:
                a.set(f"Scanning File...{i}%")
                root.update()
                time.sleep(0.25)
            else:
                a.set(f"Scanning File...{i}%")
                root.update()
                time.sleep(0.01)

        root.destroy()

def of():
    os.startfile("Run-WorkShop\Completed-Projects\Entry Form_by-Lakshya\Entries.txt")

Button(root,text="Add File",font=f1,bg="black",fg="orange",bd=5,command=af).pack(padx=100,pady=25,fill="x")
Button(root,text="Open File",font=f1,bg="black",fg="orange",bd=5,command=of).pack(padx=100,pady=25,fill="x")



root.mainloop()

if pass2==True:
    root2=Tk()

    root2.geometry("480x640")
    root2.maxsize(480,640)
    root2.maxsize(480,640)

    root2.title("Enter Entries -by Lakshya")

    root2.config(bg="orange")

    f=tkinter.font.Font( family ="Times", size = 50,  weight ="bold",underline =1)
    top=StringVar()
    top.set("Entries Form")
    Label(root2,textvariable=top,font=f,bg="orange",fg="blue").pack(padx=10,pady=15,fill="x")

    Label(root2,text="",font=f1,bg="orange").pack(padx=10,pady=15,fill="x")

    # ent={}
    # entries=file
    # fe=open(entries,"rt")
    # ent=fe.read()
    # fe.close()

    ent={}
    entries=file
    fe=open(entries,"rt+")
    filext=fe.read()
    if filext.isspace() or filext==None or filext=="" or filext=="\n":
        cfilext=False
        fe.write("")
    else:
        cfilext=True
    fe.close()


    
    no=IntVar()
    no.set("1")
    name=StringVar()
    age=IntVar()

    F=Frame(root2,bg="orange")
    F1=Frame(root2,bg="orange")
    F2=Frame(root2,bg="orange")

    Label(F,text="Number",font=f1,bg="orange",fg="blue").pack(side=LEFT,padx=10,pady=5)
    Entry(F,textvariable=no,font=f1,bg="yellow",fg="red").pack(padx=10,pady=5)
    
    Label(F1,text="Name   ",font=f1,bg="orange",fg="blue").pack(side=LEFT,padx=10,pady=5)
    Entry(F1,textvariable=name,font=f1,bg="yellow",fg="red").pack(padx=10,pady=5)
    
    Label(F2,text="Age      ",font=f1,bg="orange",fg="blue").pack(side=LEFT,padx=10,pady=5)
    Entry(F2,textvariable=age,font=f1,bg="yellow",fg="red").pack(padx=10,pady=5)
    
    F.pack(fill=X)
    F1.pack(fill=X)
    F2.pack(fill=X)


    def reset():
        name.set("")
        age.set(0)
        top.set("Reset")
        root2.update()
        time.sleep(1)
        top.set("Entries Form")
        root2.update()

    def add():
        global ent
        if no.get()<=0:
            tm.showerror("Error Occured[Er-01]","Only Whole Number allowed in Number Section")
        else:
            if no.get() in ent:
                 tm.showerror("Error Occured[Er-02]","Number already Exist")
            else:
                ent[no.get()] = {"Name":name.get(),"Age":age.get()}
                no.set(no.get()+1)
                name.set("")
                age.set(0)
                top.set("Added")
                root2.update()
                time.sleep(0.5)
                top.set("Entries Form")
                root2.update()

    def save():
        global ent
        if cfilext==True:
            orwtrperm=tm.askquestion("Existing Data Found",f"We found Some existing Data in Your Given File({file})\n\
            Do you want to Overwrite?")
            if orwtrperm.lower()=="yes":
                fe=open(entries,"at")
            else:
                fe=open(entries,"wt")           
        else:
            fe=open(entries,"wt")
        fe.write(json.dumps(ent))
        fe.close()

        tm.showinfo("File Modified","Your File is Saved")
        root2.mainloop()

    def ex():
        root2.mainloop()

    def of2():
        os.startfile("F:/Coding/python/Lakshya/RUN-Support/No of Entries.txt")

    f2=tkinter.font.Font( size = 30,  weight ="bold")
    F3=Frame(root2,bg="orange")
    Button(F3,text="Add",font=f2,bg="blue",fg="white",padx=50,command=add).pack(side=LEFT,padx=20,pady=15)
    Button(F3,text="Reset",font=f2,bg="blue",fg="white",padx=50,command=reset).pack(padx=20,pady=15)
    F3.pack(fill=X)
    F4=Frame(root2,bg="orange")
    Button(F4,text="Save",font=f2,bg="Red",fg="White",padx=50,command=save,relief=RAISED).pack(fill=X,padx=20)
    F4.pack(fill=X)
    F5=Frame(root2,bg="orange")
    Button(F5,text="View File",font=f2,bg="Red",fg="White",padx=50,command=of2,relief=RAISED).pack(side=LEFT,padx=10)
    Button(F5,text="Close",font=f2,bg="Black",fg="Yellow",padx=10,command=ex,relief=RAISED).pack(side=RIGHT,padx=10)
    F5.pack(fill=X,side=BOTTOM,pady=10)


    root2.mainloop()