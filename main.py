from tkinter import *
from asia import Asia
from america import America
from africa import Africa
from europe import Europe
import random, time

root = Tk()


class App:
    BACKGROUD_COLOR = ['#ff4000', '#ff8000', "#ffbf00", '#00ff40', '#00ffbf', '#8000ff', '#ffcccc']

    def __init__(self, master) -> None:
        self.title = master.title('Clock')
        self.geometry = master.geometry('650x250')
        #self.resize = master.resizable(0,0)
        #self.background = master.configure(bg=random.choice(App.BACKGROUD_COLOR))
        

        #Display Button
        self.btn = Button(master, text="Display", command=self.display)
        self.btn.grid(column=8, row=5)

        self.clear_btn = Button(master, text="Clear", command=self.clear)
        self.clear_btn.grid(column=9, row=5)


        inner_frame = Frame(master, padx=75, pady=50)
        inner_frame.grid(column=0, row=4, columnspan=3, rowspan=2, padx=10, pady=10)

        #BACKGROUD_COLOR = ['#ff4000', '#ff8000', "#ffbf00", '#00ff40', '#00ffbf', '#8000ff', 'ff00ff', '#ffcccc']

        #time label insde the frame
        self.lbl = Label(inner_frame, font=('Arial', 30, 'bold'),
                    background=random.choice(App.BACKGROUD_COLOR), foreground='white')
        self.lbl.pack(anchor='center')


        self.NorthAmerica = StringVar()
        #cities in North America dropdown list options       NA -> North America
        self.NA_cities_options = ["Port-Au-Prince", "Toronto", "Vancouver", "Winnipeg", "Edmonton", "Sao Paulo", 
                                  "Los Angeles", "New York", "Rio Branco", "Mexico City", "Lima", "Buenos Aires", "*"]
        #NA timezome menu
        self.NorthAmerica_tz_menu = OptionMenu(master, self.NorthAmerica, *self.NA_cities_options)
        Label(master, text="North America").grid(column=8, row=0)
        self.NorthAmerica_tz_menu.grid(column=8, row=1)
     
        #Asia
        self.ASIA = StringVar()
        self._Asia_cities_options = ["Honkong", "Seoul", "Tokyo", "Jerusalem", "Shanghai", 
                                     "Singapore", "Macao", "Vientiane", "Dili", "Istanbul", "*"]
        self._Asia_tz_menu = OptionMenu(master, self.ASIA, *self._Asia_cities_options)
        Label(master, text="Asia").grid(column=9, row=0)
        self._Asia_tz_menu.grid(column=9, row=1)

        #Europe
        self.EUROPE = StringVar()
        self._Europe_cities_option = ["Madrid", "London", "Berlin", "Amsterdam", "Rome", "Paris", 
                                      "Lisbon", "Moscow", "Kiev", "Monaco", "Bucharest", "*"]
        self._Europe_tz_menu = OptionMenu(master, self.EUROPE, *self._Europe_cities_option)
        Label(master, text="Europe").grid(column=8, row=2)
        self._Europe_tz_menu.grid(column=8, row=3)
   
       
        #AFRICA
        self.AFRICA = StringVar()
        self._Africa_cities_option = ["Lagos", "Nairobi", "Malabo", "Windhoek", "Freetown", "Bissau",
                                      "Johannesburg", "Libreville", "Douala", "Khartoum", "Kinshasa", "*"]
        self._Africa_tz_menu = OptionMenu(master, self.AFRICA, *self._Africa_cities_option)
        Label(master, text="Africa").grid(column=9, row=2)
        self._Africa_tz_menu.grid(column=9, row=3)


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

        elif self.NorthAmerica.get() == 'New York':
            return f'{America.New_York()}'
        
        elif self.NorthAmerica.get() == 'Rio Branco':
            return f'{America.Rio_Branco()}'
        
        elif self.NorthAmerica.get() == 'Mexico City':
            return f'{America.Mexico_City()}'
        
        elif self.NorthAmerica.get() == 'Lima':
            return f'{America.Lima()}'
        
        elif self.NorthAmerica.get() == 'Buenos Aires':
            return f'{America.Buenos_Aires()}'
        
        elif self.NorthAmerica == '*':
            return None
        
        #ASIA
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
        
        elif self.ASIA.get() == 'Singapore':
            return f'{Asia.Singapore()}'
        
        elif self.ASIA.get() == 'Macao':
            return f'{Asia.Macao()}'
        
        elif self.ASIA.get() == 'Vientiane':
            return f'{Asia.Vientiane()}'
        
        elif self.ASIA.get() == 'Dili':
            return f'{Asia.Dili()}'
        
        elif self.ASIA.get() == 'Istanbul':
            return f'{Asia.Istanbul()}'
        
        elif self.ASIA == '*':
            return None
        
        #EUROPE
        elif self.EUROPE.get() == "Madrid":
            return f'{Europe.Madrid()}'
        
        elif self.EUROPE.get() == "London":
            return f'{Europe.London()}'
        
        elif self.EUROPE.get() == "Berlin":
            return f'{Europe.Berlin()}'
        
        elif self.EUROPE.get() == "Amsterdam":
            return f'{Europe.Amsterdam()}'
        
        elif self.EUROPE.get() == "Rome":
            return f'{Europe.Rome()}'
        
        elif self.EUROPE.get() == "Paris":
            return f'{Europe.Paris()}'
        
        elif self.EUROPE.get() == "Lisbon":
            return f'{Europe.Lisbon()}'
        
        elif self.EUROPE.get() == "Moscow":
            return f'{Europe.Moscow()}'
        
        elif self.EUROPE.get() == "Monaco":
            return f'{Europe.Monaco()}'
        
        elif self.EUROPE.get() == "Bucharest":
            return f'{Europe.Bucharest()}'
        
        elif self.EUROPE.get() == "Kiev":
            return f'{Europe.Kiev()}'
        
        elif self.EUROPE == '*':
            return None
        
        #AFRICA
        elif self.AFRICA.get() == "Lagos":
            return f'{Africa.Lagos()}'
        
        elif self.AFRICA.get() == "Nairobi":
            return f'{Africa.Nairobi()}'

        elif self.AFRICA.get() == "Malabo":
            return f'{Africa.Malabo()}'

        elif self.AFRICA.get() == "Windhoek":
            return f'{Africa.Windhoek()}'

        elif self.AFRICA.get() == "Freetown":
            return f'{Africa.Freetown()}'

        elif self.AFRICA.get() == "Bissau":
            return f'{Africa.Bissau()}'

        elif self.AFRICA.get() == "Johannesburg":
            return f'{Africa.Johannesburg()}'

        elif self.AFRICA.get() == "Libreville":
            return f'{Africa.Libreville()}'

        elif self.AFRICA.get() == "Douala":
            return f'{Africa.Douala()}'

        elif self.AFRICA.get() == "Khartoum":
            return f'{Africa.Khartoum()}'

        elif self.AFRICA.get() == "Kinshasa":
            return f'{Africa.Kinshasa()}'
                
        elif self.AFRICA == '*':
            return None
        
  
    def __str__(self) -> str:
        return f'{self.time_in_cities()}'
a = App(root)
root.mainloop()