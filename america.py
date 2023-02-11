import datetime, pytz, time


class America:
    def Port_au_Prince():
        now =datetime.datetime.now(tz=pytz.timezone('America/Port-au-Prince'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Toronto():
        now =datetime.datetime.now(tz=pytz.timezone('America/Toronto'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time

    def Vancouver():
        now =datetime.datetime.now(tz=pytz.timezone('America/Vancouver'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    #['Vancouver', 'Winnipeg', 'Edmonton', 'Sao_Paulo', 'Los_Angeles', 'New_York']

    def Winnipeg():
        now =datetime.datetime.now(tz=pytz.timezone('America/Winnipeg'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Edmonton():
        now =datetime.datetime.now(tz=pytz.timezone('America/Edmonton'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time

    def Sao_Paulo():
        now =datetime.datetime.now(tz=pytz.timezone('America/Sao_Paulo'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Los_Angeles():
        now =datetime.datetime.now(tz=pytz.timezone('America/Los_Angeles'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def New_York():
        now =datetime.datetime.now(tz=pytz.timezone('America/New_York'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time


#["Port-Au-Prince", "Toronto", "Vancouver", "Winipeg", "Edmonton", "Sao Paulo", "Los Angeles", "New York"]

