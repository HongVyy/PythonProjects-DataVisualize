import tkinter as tk
#from tkinter import ttk
#test ttkbootstrap theme
import ttkbootstrap as ttk

def convert():
    mile_input = entryInt.get()
    km_output = mile_input * 1.61
    output_string.set(km_output)

#window
window = ttk.Window(themename ='journal')
window.title('Demo')
window.geometry('300x150')

#title
title_label = ttk.Label(master = window, text ='Miles to kilometers', font='Calibri 20 bold')
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entryInt = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable = entryInt)

input_frame2 = ttk.Frame(master = window)
entryInt2 = tk.IntVar()
entry2 = ttk.Entry(master = input_frame, textvariable = entryInt)

input_frame3 = ttk.Frame(master = window)
entryInt3 = tk.IntVar()
entry3 = ttk.Entry(master = input_frame, textvariable = entryInt)

button = ttk.Button(master = input_frame, text = 'Convert', command = convert)
entry.pack(side = 'left', padx = 10)
button.pack(side = 'left')
input_frame.pack(pady = 10)

#output
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text ='Output', font = 'Calibri 20', textvariable = output_string)
output_label.pack(pady = 5)

#run
window.mainloop()
