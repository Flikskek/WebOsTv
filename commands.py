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