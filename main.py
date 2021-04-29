from tkinter import * 

from store import tvkey
from pywebostv.discovery import *    # Because I'm lazy, don't do this.
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
    system.power_off()

def notify():
    system.notify('Hello :D')


root = Tk()
root.title("LGTV")
 
vup = Button(text="Volume up", command=volup)
vdown = Button(text="Volume down", command=voldown)
chup = Button(text="Channel up", command=chup)
chdown = Button(text="Channel down", command=chdown)
poff = Button(text="Power Off", command=poff)
notify = Button(text="Test Notify", command=notify)
                           

chdown.pack()
chup.pack()
vdown.pack()
vup.pack()
poff.pack()
notify.pack()

store = tvkey #TV key


client = WebOSClient("192.168.0.104")
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