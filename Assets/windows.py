import tkinter as tk
import ttkbootstrap as ttk
import threading

def _showabout():
    window = tk.Tk()
    window.title("PyMC-Server - About")
    window.resizable(False,False)
    window.geometry("600x400")
    n = ttk.Notebook(window)
    frame1 = ttk.Frame(master=n)
    frame2 = ttk.Frame(master=n)
    n.add(frame1,text="About")
    n.add(frame2,text="Credits")
    n.pack()
    t = ttk.Text(master=frame1)
    t.pack()
    t.insert("1.0","""PyMC-Server

This is an application that installs on minecraft server for free for you.
You can manage and make new servers with no ads and no in-app purchases. This is not just a server installer its a manager and maker
this application will install PaperMC server which its SUPER FAST!!!
             
Made and maintained by @mas6y6 on github
""")
    t.config(state='disabled')

    t2 = ttk.Text(master=frame2)
    t2.pack()
    t2.insert("1.0","""
Sounds by 'UNIVERSFIELD' on Pixabay

SoundPlayer (playsound) by TaylorSMarks on PyPI and Tony1527 on Github

WindowInterface (ttkbootstrap) by israel.dryer on PyPI and Github

Requester (requests) by graffatcolmingov, Lukasa and nateprewitt on PyPI
""")
    t2.config(state='disabled')
    window.mainloop()

def running():
    window = tk.Tk()
    window.title("PyMC-Server - About")
    window.resizable(False,False)
    window.geometry("600x300")
    t = ttk.Text(master=window)
    t.pack()
    t.insert("1.0","""The server is currently active
""")
    t.config(state='disabled')
    window.mainloop()

def showabout():
    threading.Thread(_showabout()).start()
