import datetime, pytz, time


class Europe:
    def Madrid():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Madrid'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def London():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/London'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time

    def Berlin():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Berlin'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Amsterdam():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Amsterdam'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Rome():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Rome'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Paris():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Paris'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Lisbon():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Lisbon'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Moscow():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Moscow'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Kiev():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Kiev'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Monaco():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Monaco'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Bucharest():
        now =datetime.datetime.now(tz=pytz.timezone('Europe/Bucharest'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
#["Madrid", "London", "Berlin", "Amsterdam", "Rome", "Paris", "Lisbon", "Moscow", "Kiev", "Monaco", "Bucharest"]



myFile = "timezones.txt"
with open(myFile, "w") as f:
    for tz in pytz.all_timezones:
        f.writelines(tz+"\n")