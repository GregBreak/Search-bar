import webbrowser
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def search(event):
    url="https://www.google.it/search?q="+e.get()
    webbrowser.open(url)

def disable_event():
   pass

def close_win(exx):
   root.destroy()

root = ttk.Window(themename="darkly")
root.title("My Search Bar")

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
px = ws-200
py = hs-120

root.geometry("+%d+%d" %(px,py))
root.attributes('-alpha',0.5)
root.attributes('-topmost', True)
root.config(menu=None)

e = ttk.Entry()
e.pack(side=LEFT, padx=5, pady=10)
e.focus()

b1 = ttk.Button(root, text="Search", bootstyle="success",command=search)
b1.pack(side=LEFT, padx=5, pady=10)
b1.pack_forget()

root.bind('<Return>',search)
root.bind('<Escape>', lambda exx: close_win(exx))
#root.protocol("WM_DELETE_WINDOW", disable_event)
root.overrideredirect(True)
root.mainloop()