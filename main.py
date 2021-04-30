from tkinter import * 
from PIL import ImageTk

from store import tvkey,ip

import time

from pywebostv.discovery import *    
from pywebostv.connection import *
from pywebostv.controls import *

def volup():
    media.volume_up()

def voldown():
    media.volume_down()

def chup():
    tv_control.channel_up()

def chdown():
    tv_control.channel_down()


def poff():
    count=4
    while count!=1:
        count=count-1
        system.notify('Power off ' + str(count) + '...')
        time.sleep(1)
    system.power_off()

def notify():
    system.notify('Hello :D')


root = Tk()
root.title("LGTV")
 
vup = Button(text="Volume up", command=volup,background="#555", foreground="#ccc", relief='flat')
vdown = Button(text="Volume down", command=voldown,background="#555", foreground="#ccc", relief='flat')
chup = Button(text="Channel up", command=chup,background="#555", foreground="#ccc", relief='flat',)
chdown = Button(text="Channel down", command=chdown,background="#555", foreground="#ccc", relief='flat')
poff = Button(text="Power Off", command=poff,background="#555", foreground="#ccc", relief='flat')
notify = Button(text="Test Notify", command=notify,background="#555", foreground="#ccc", relief='flat')
                           

chdown.pack()
chup.pack()
vdown.pack()
vup.pack()
poff.pack()
notify.pack()

store = tvkey #TV key


client = WebOSClient(ip)
client.connect()

media = MediaControl(client)
tv_control = TvControl(client)
system = SystemControl(client)


for status in client.register(store):
    if status == WebOSClient.PROMPTED:
        print("Please accept the connect on the TV!")
    elif status == WebOSClient.REGISTERED:
        print("Registration successful!")

root.mainloop()