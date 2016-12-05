from Tkinter import *
from tkFileDialog import *

filename=None

def newFile():
    global filename
    filename= "Untitled"
    text.delete(0.0, END) #0.0 represents row and column number

"""def saveFile():
    global filename
    t = text.get(0.0, END)
    f = open(filename, 'w')
    f.write(t)
    f.close()"""
    #Currently save block is not working
    #The program tries to save file but it cant due to preexisting file

def saveAs():
    f=asksaveasfile(defaultextension='.txt')
    t=text.get(0.0,END)
    try:
        f.write(t.rstrip())
    except:
        showerror(title="Oops!",message="Unable to save file...")

def openFile():
    global filename
    #file=askopenfile(parent=root,title='Select a file')
    f=askopenfile(mode='r')
    t=f.read()
    text.delete(0.0,END)
    text.insert(0.0,t)

root=Tk()
root.title("Simple editor")
root.minsize(width=400,height=400)
root.maxsize(width=400,height=400)
#Fixed size of the window
text=Text(root,width=400,height=400)
text.pack()

menubar=Menu(root)
filemenu=Menu(menubar)
filemenu.add_command(label="New",command=newFile)
filemenu.add_command(label="Open",command=openFile)
#filemenu.add_command(label="Save",command=saveFile)
filemenu.add_command(label="Save",command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Quit",command=root.quit)
menubar.add_cascade(label="File",menu=filemenu)

root.config(menu=menubar)
root.mainloop()
