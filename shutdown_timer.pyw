import os
import tkinter as tk

def on_click():
    num_hour = hour_ent.get()
    num_min = minute_ent.get()
    num_sec = second_ent.get()
    
    window.destroy()
    
    if num_hour == '':
        num_hour = 0
    if num_min == '':
        num_min = 0
    if num_sec == '':
        num_sec = 0
    
    total = (int(num_hour) * 3600) + (int(num_min) * 60) + int(num_sec)
    
    print(total)
    
    os.system(f'cmd /c "C:\Windows\System32\shutdown.exe -s -t {total}"')

window = tk.Tk()
window.title("Shutdown Timer")
hour_frame = tk.Frame()
hour_lab = tk.Label(master=hour_frame, text="Hours")
hour_lab.grid(row=0, column=0, sticky="e")
hour_ent = tk.Entry(master=hour_frame)
hour_ent.grid(row=0, column=1, sticky="w")

minute_frame = tk.Frame()
minute_lab = tk.Label(master=minute_frame, text="Minutes")
minute_lab.grid(row=1, column=0, sticky="e")
minute_ent = tk.Entry(master=minute_frame)
minute_ent.grid(row=1, column=1, sticky="w")

second_frame = tk.Frame()
second_lab = tk.Label(master=second_frame, text="Seconds")
second_lab.grid(row=2, column=0, sticky="e")
second_ent = tk.Entry(master=second_frame)
second_ent.grid(row=2, column=1, sticky="w")

button = tk.Button(master=window, text="Start Shutdown Timer", command=on_click)

hour_frame.pack()
minute_frame.pack()
second_frame.pack()
button.pack()

window.mainloop()
