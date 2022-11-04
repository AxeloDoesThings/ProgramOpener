import tkinter as tk
from tkinter import filedialog, Text
import os

screen_height = 700
screen_width = 700
ProgramVer = "1.2"

root = tk.Tk()
root.title("Program Opener " + ProgramVer)
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps =  f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def OpenDir():
    for widget in LabelFrame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)

    for app in apps:
        if app == "":
            apps.remove(app)

    for app in apps:
        label = tk.Label(LabelFrame, text=app)
        label.pack()

def OpenDirSpecific():
    for widget in LabelFrame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir=InputBox.get(), title="Select File", 
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)

    for app in apps:
        label = tk.Label(LabelFrame, text=app)
        label.pack()

def OpenApp():
    for app in apps:
        os.startfile(app)

def RemoveApp():
    for widget in LabelFrame.winfo_children():
        widget.destroy()

    apps.pop()

    for app in apps:
        label = tk.Label(LabelFrame, text=app)
        label.pack()

def ClearList():
    for widget in LabelFrame.winfo_children():
        widget.destroy()

    for numapp in range(0, len(apps)):
        apps.pop()


canvas = tk.Canvas(root, width=900, height=700, bg="#002e22")
canvas.pack()

frame = tk.Frame(canvas, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

LabelFrame = tk.Frame(frame, bg="#b5b5b5")
LabelFrame.place(relwidth=0.6, relheight=0.75, relx=0.3, rely=0.1)

ButtonElement = tk.Frame(canvas, bg="white")
ButtonElement.place(relwidth=0.2, relheight=0.2, relx=0.1, rely=0.2)

OpenDirectory = tk.Button(ButtonElement, text="Open Dir", width=10, height=1, fg="white", bg="green", command=OpenDir)
OpenDirectory.pack()

OpenApps = tk.Button(ButtonElement, text="Open Apps", width=10, height=1, fg="white", bg="green", command=OpenApp)
OpenApps.pack()

RemoveAppButton = tk.Button(ButtonElement, text="Remove App", width=10, height=1, fg="white", bg="green", command=RemoveApp)
RemoveAppButton.pack()

ClearListButton = tk.Button(ButtonElement, text="Clear List", width=10, height=1, fg="white", bg="green", command=ClearList)
ClearListButton.pack()

InputBox = tk.Entry(root, borderwidth=5, fg="black")
InputBox.pack()

OpenDirectorySpec = tk.Button(root, text="Open Specific Directory", padx=10, pady=5, fg="white", bg="green", command=OpenDirSpecific)
OpenDirectorySpec.pack()

for app in apps:
    label = tk.Label(LabelFrame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')