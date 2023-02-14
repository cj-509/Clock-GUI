from tkinter import *
from asia import Asia
from america import America
import random, time

root = Tk()


class App:
    BACKGROUD_COLOR = ['#ff4000', '#ff8000', "#ffbf00", '#00ff40', '#00ffbf', '#8000ff', '#ffcccc']

    def __init__(self, master) -> None:
        self.title = master.title('Clock')
        self.geometry = master.geometry('800x400')

        #Display Button
        self.btn = Button(master, text="Display", command=self.display)
        self.btn.grid(column=8, row=7)

        self.clear_btn = Button(master, text="Clear", command=self.clear)
        self.clear_btn.grid(column=9, row=7)


        inner_frame = Frame(master, padx=75, pady=50)
        inner_frame.grid(column=0, row=2, columnspan=4, rowspan=2, padx=10, pady=10)

        #BACKGROUD_COLOR = ['#ff4000', '#ff8000', "#ffbf00", '#00ff40', '#00ffbf', '#8000ff', 'ff00ff', '#ffcccc']

        #time label insde the frame
        self.lbl = Label(inner_frame, font=('Arial', 30, 'bold'),
                    background=random.choice(App.BACKGROUD_COLOR), foreground='white')
        self.lbl.pack(anchor='center')


        self.NorthAmerica = StringVar()
        #cities in North America dropdown list options       NA -> North America
        self.NA_cities_options = ["Port-Au-Prince", "Toronto", "Vancouver", "Winnipeg", 
                          "Edmonton", "Sao Paulo", "Los Angeles", "New York", "*"]
        
        #NA timezome menu
        self.NorthAmerica_tz_menu = OptionMenu(master, self.NorthAmerica, *self.NA_cities_options)
        Label(master, text="North America").grid(column=6, row=0)
        self.NorthAmerica_tz_menu.grid(column=6, row=1)
     

        self.ASIA = StringVar()
        #
        self._Asia_cities_options = ["Honkong", "Seoul", "Tokyo", "Jerusalem", "Shanghai"]
        self._Asia_tz_menu = OptionMenu(master, self.ASIA, *self._Asia_cities_options)
        Label(master, text="Asia").grid(column=7, row=0)
        self._Asia_tz_menu.grid(column=7, row=1)
   
        #user intput
        #self.entry = Entry(master, borderwidth=3, width=25)
        #self.entry.grid(row=0, column=0)
    def display(self):
        string = self.time_in_cities()
        self.lbl.config(text=string)
        self.lbl.after(1000, self.display)
        self.lbl.pack()
        #self.btn['state'] = DISABLED
    
    def clear(self):
        self.lbl.after(1000, self.lbl.destroy())
       # self.btn['state'] = NORMAL

    
    def time_in_cities(self):
        if self.NorthAmerica.get() == 'Port-Au-Prince':
            return f'{America.Port_au_Prince()}'
        
        elif self.NorthAmerica.get() == 'Toronto':
            return f'{America.Toronto()}'
        
        elif self.NorthAmerica.get() == 'Vancouver':
            return f'{America.Vancouver()}'
        
        elif self.NorthAmerica.get() == 'Winnipeg':
            return f'{America.Winnipeg()}'
        
        elif self.NorthAmerica.get() == 'Edmonton':
            return f'{America.Edmonton()}'
        
        elif self.NorthAmerica.get() == 'Sao Paulo':
            return f'{America.Sao_Paulo()}'
        
        elif self.NorthAmerica.get() == 'Los Angeles':
            return f'{America.Los_Angeles()}'
        elif self.NorthAmerica == '*':
            return None
        elif self.NorthAmerica.get() == 'New York':
            return f'{America.New_York()}'
        #END

        elif self.ASIA.get() == 'Honkong':
            return f'{Asia.Hong_Kong()}'
        
        elif self.ASIA.get() == 'Seoul':
            return f'{Asia.Seoul()}'
        
        elif self.ASIA.get() == 'Tokyo':
            return f'{Asia.Tokyo()}'
        
        elif self.ASIA.get() == 'Jerusalem':
            return f'{Asia.Jerusalem()}'
        
        elif self.ASIA.get() == 'Shanghai':
            return f'{Asia.Shanghai()}'
  
    def __str__(self) -> str:
        return f'{self.time_in_cities()}'
a = App(root)
root.mainloop()