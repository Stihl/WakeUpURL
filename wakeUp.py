#EVENT TIMER SCRIPT

import webbrowser
import time
from datetime import datetime
alive = True

class Timer:
    hour = 0
    minute = 0
    url = "URL"
    done = False
    def __init__(self,hour,minute,url,done):
        self.hour = hour
        self.minute = minute
        self.url = url
        self.done = done
    def reset_timer(self):
        self.done = False
    #Add timers special function so it can do something other than launch a webbrowser
        
now = datetime.now().time()
start_time = datetime.now()
total_hours = 0
timers = []

timers.append(Timer(6,18,"URL",False))
timers.append(Timer(6,30,"URL",False))
timers.append(Timer(18,30,"URL",False))

while alive:
    now = datetime.now().time()
    total_hours = (datetime.now() - start_time).total_seconds() / 60 / 60
    print(f"\n-------------------------------\nTotal Hours Ran: {total_hours:.2f}")
    print(f"The Time is: {now}")

    for timer in timers:
        if(timer.done != True):
            print("NOT DONE - TITLE - Hour ", timer.hour, ", Minute: ", timer.minute)
        else:
            print("Done")
    #Make a string interpreter parses out the time in hours, minutes, and seconds.
    #Also give this thing a UI (event if its commandline) with a text entry for the URLs and times and a database so the timers aren't hardcoded, SQLite3 will do for now.

    if(now.hour == 23 and now.minute > 59):
        for timer in timers:
            timer.reset_timer()
    
    for timer in timers:
        if(now.hour == timer.hour and timer.done != True):
            if(now.minute > timer.minute):
                webbrowser.open(timer.url, new=1, autoraise=True)
                timer.done = True
                 
    
    time.sleep(5)
    


        
