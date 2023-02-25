import datetime, pytz, time
from america import America

class Asia:
    def Hong_Kong():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Hong_Kong'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Seoul():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Seoul'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Tokyo():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Tokyo'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Jerusalem():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Jerusalem'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Shanghai():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Shanghai'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Singapore():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Singapore'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Macao():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Macao'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Vientiane():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Vientiane'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Dili():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Dili'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    def Istanbul():
        now =datetime.datetime.now(tz=pytz.timezone('Asia/Istanbul'))
        current_time = now.strftime("%I:%M:%S %p")
        return current_time
    
    
#["Honkong", "Seoul", "Tokyo", "Jerusalem", "Shanghai"]
'''
{"HongKong": Asia.Hong_Kong(),
 "Seoul": Asia.Seoul(),
 "Tokyo":Asia.Tokyo(),
 "Jerusalem": Asia.Jerusalem(),
 "Shangai": Asia.Shanghai()}
 '''

