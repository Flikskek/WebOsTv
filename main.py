from tkinter import * 



from store import tvkey,ip

import commands as com

import time

from pywebostv.discovery import *    
from pywebostv.connection import *
from pywebostv.controls import *


root = Tk()
root.title("LGTV")
root.geometry("485x600")

vup = Button(text="Volume up", command=com.volup, background="#555", foreground="#ccc")
vdown = Button(text="Volume down", command=com.voldown, background="#555", foreground="#ccc")
chup = Button(text="Channel up", command=com.chup, background="#555", foreground="#ccc")
chdown = Button(text="Channel down", command=com.chdown, background="#555", foreground="#ccc")
poff = Button(text="Power Off", command=com.poff, background="#555", foreground="#ccc")
notify = Button(text="Test Notify", command=com.notify ,background="#555", foreground="#ccc")
                           

chdown.place(x=400,y=250)
chup.place(x=400,y=225)
vdown.place(x=0,y=250)
vup.place(x=0,y=225)
poff.place(x=225,y=0)
notify.place(x=225,y=550)

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