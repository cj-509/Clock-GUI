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
    
#["Honkong", "Seoul", "Tokyo", "Jerusalem", "Shanghai"]
'''
{"HongKong": Asia.Hong_Kong(),
 "Seoul": Asia.Seoul(),
 "Tokyo":Asia.Tokyo(),
 "Jerusalem": Asia.Jerusalem(),
 "Shangai": Asia.Shanghai()}
 '''

