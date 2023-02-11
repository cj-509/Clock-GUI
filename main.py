from tkinter.ttk import *
from tkinter import *
from asia import Asia
from america import America
import time




root = Tk()

root.title(" GUI Clock")
root.geometry("600x250")

#create a frame to display the time
frame = LabelFrame(root, padx=75, pady=50)
frame.grid(column=0, row=2, columnspan=5, rowspan=3, padx=10, pady=10)


time_zones = {"Port-Au-Prince": America.Port_au_Prince(), 
             "Toronto": America.Toronto(), 
             "Vancouver": America.Vancouver(), 
             "Winipeg": America.Winnipeg(), 
             "Edmonton": America.Edmonton(), 
             "Sao Paulo": America.Sao_Paulo(),
             "Los Angeles": America.Los_Angeles(),
             "New York": America.New_York(),
             "HongKong": Asia.Hong_Kong(),
             "Seoul": Asia.Seoul(),
             "Tokyo":Asia.Tokyo(),
             "Jerusalem": Asia.Jerusalem(),
             "Shanghai": Asia.Shanghai()}


#create display function
def display():
    NA_city = NortAmerica.get()

    # _Asia.get refers to StringVar()
    Asia_city = _Asia.get()

    for key in time_zones:
        if key == NA_city or key == Asia_city:
           global current_time
           current_time = Label(frame, font=("calibri", 20, "bold"), background="purple")
    current_time.config(text=str(time_zones[key]))
    #current_time.after(1000, display)
    current_time.pack()

# clear funtion initialize
def clear():
    current_time.after(1000, current_time.destroy())



NortAmerica = StringVar()

#cities in North America dropdown list options       NA -> North America
NA_cities_options = ["Port-Au-Prince", "Toronto", "Vancouver", "Winipeg", 
                          "Edmonton", "Sao Paulo", "Los Angeles", "New York"]
#shows menu
NortAmerica_tz_menu = OptionMenu(root, NortAmerica, *NA_cities_options)
Label(root, text="North America").grid(column=7, row=0)
NortAmerica_tz_menu.grid(column=7, row=1)

_Asia = StringVar()

#citeis in asia dropdown list options 
_Asia_cities_options = ["Honkong", "Seoul", "Tokyo", "Jerusalem", "Shanghai"]

_Asia_tz_menu = OptionMenu(root, _Asia, *_Asia_cities_options)
Label(root, text="Asia").grid(column=8, row=0)
_Asia_tz_menu.grid(column=8, row=1)



#clear btn to clear text on the screen
clear_btn = Button(root, text="Clear", command=lambda: clear())
clear_btn.grid(column=6, row=7)


#display button the text inside the frame
btn = Button(root, text="Display", command=lambda: display())
btn.grid(column=7, row=7)



root,mainloop()
