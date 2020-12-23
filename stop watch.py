import tkinter as Tkinter
from datetime import datetime

#counter code
counter = 66600
running = False

def counter_label(label):
    def count():
        if running:
            global counter
            if counter == 66600:
                display = "Starting..."
            else:
                tt = datetime.fromtimestamp(counter)
                string = tt.strftime("%H:%M:%S")
                display = string

            label['text'] = display
            label.after(1000, count)
            counter += 1
    count()
#functions

def Start(label):
    global running
    running = True
    counter_label(label)
    start['state'] = 'disabled'
    stop['state'] = 'normal'
    reset['state'] = 'normal'

def Stop():
    global running
    start['state'] = 'normal'
    stop['state'] = 'disabled'
    reset['state'] = 'normal'
    running = False

def Reset(label):
    global counter
    counter = 66600
    if running == False:
        reset['state'] = 'disabled'
        label['text'] = 'Welcome!'
    else:
        label['text'] = 'Starting...'

#GUI
root = Tkinter.Tk()
root.title("Stopwatch")

root.geometry('450x150')
root.config(bg="gray")
label = Tkinter.Label(root, text="Welcome!",bg='gray', fg="red", font="Verdana 30 bold")
label.pack()
label2 = Tkinter.Label(root, text="Created by: Mannu",bg='gray', fg="white", font="Verdana 10 bold")
label2.pack(side='bottom')
f = Tkinter.Frame(root)
start = Tkinter.Button(f, text='Start', width=6,fg='red',font="Verdana 10 bold", command=lambda: Start(label))
stop = Tkinter.Button(f, text='Stop', width=6,fg='red',font="Verdana 10 bold", state='disabled', command=Stop)
reset = Tkinter.Button(f, text='Reset', width=6,fg='red',font="Verdana 10 bold", state='disabled', command=lambda: Reset(label))
f.pack(anchor='center', pady=10)
start.pack(side="left")
stop.pack(side="left")
reset.pack(side="left")
root.mainloop() 
