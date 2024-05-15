import time
from plyer import notification

TITLE_NOTIF = "Greetings from Zoz"
MESS_NOTIF = "If you see this message this means your day was fantastic <3 "

notification.notify( 
    title = TITLE_NOTIF,
    message = MESS_NOTIF,
    app_icon = None,
    timeout = 10,
    toast = False
)

time.sleep(10)

notification.notify( 
    title = "wassup",
    message = "this is a second message",
    app_icon = None,
    timeout = 10,
    toast = False  
)
