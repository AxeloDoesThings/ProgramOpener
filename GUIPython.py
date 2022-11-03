import tkinter as tk
from tkinter import filedialog, Text
import os

screen_height = 700
screen_width = 700

root = tk.Tk()
apps = []

if os.path.isfile('save.txt'):
    with open('save.txt', 'r') as f:
        tempApps =  f.read()
        tempApps = tempApps.split(',')
        apps = [x for x in tempApps if x.strip()]


def OpenDir():
    for widget in frame.winfo_children():
        widget.destroy()
    
    filename = filedialog.askopenfilename(initialdir="/", title="Select File", 
    filetypes=(("executables", "*.exe"), ("all files", "*.*")))

    apps.append(filename)

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

def OpenApp():
    for app in apps:
        os.startfile(app)

def RemoveApp():
    for widget in frame.winfo_children():
        widget.destroy()

    apps.pop()

    for app in apps:
        label = tk.Label(frame, text=app)
        label.pack()

canvas = tk.Canvas(root, width=screen_height, height=screen_width, bg="#002e22")
canvas.pack()

frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

button_element = tk.Frame(root, bg="white")
button_element.place(relwidth=0.2, relheight=0.2, relx=0.1, rely=0.2)

OpenDirectory = tk.Button(button_element, text="Open Dir", padx=10, pady=5, fg="white", bg="green", command=OpenDir)
OpenDirectory.pack()

OpenApps = tk.Button(button_element, text="Open Apps", padx=10, pady=5, fg="white", bg="green", command=OpenApp)
OpenApps.pack()

RemoveApp = tk.Button(button_element, text="Remove App", padx=10, pady=5, fg="white", bg="green", command=RemoveApp)
RemoveApp.pack()


for app in apps:
    label = tk.Label(frame, text=app)
    label.pack()

root.mainloop()

with open('save.txt', 'w') as f:
    for app in apps:
        f.write(app + ',')