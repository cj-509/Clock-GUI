import datetime, pytz, time


class Africa:
    def Lagos():
        now =datetime.datetime.now(tz=pytz.timezone('Africa/Lagos'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Nairobi():
        now =datetime.datetime.now(tz=pytz.timezone('Africa/Nairobi'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Malabo():
        now =datetime.datetime.now(tz=pytz.timezone('Africa/Malabo'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Windhoek():
        now =datetime.datetime.now(tz=pytz.timezone('Africa/Windhoek'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Freetown():
        now =datetime.datetime.now(tz=pytz.timezone('Africa/Freetown'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time

#["Lagos", "Nairobi", "Malabo", "Windhoek", "Freetown"]