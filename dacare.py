try:
    from plyer import notification
    from plyer.utils import platform
    from plyer.compat import PY2
except ImportError as ex:
    print(ex)
    print("This app uses plyer for sending notifications. "
          "Please install plyer with this command - 'python -m pip install plyer'")
    import sys
    sys.exit(1)

import os
import time
import random
import pyttsx3
import webbrowser

videos = ['https://www.youtube.com/watch?v=GSO6g3dNR7s',
          'https://www.youtube.com/watch?v=Y2dHYfb5OnE',
          'https://www.youtube.com/watch?v=uiKg6JfS658',
          'https://www.youtube.com/watch?v=azCzW_0GADM']

engine = pyttsx3.init()
engine.setProperty('rate', 150)
voices = engine.getProperty('voices')
for voice in voices:
    engine.setProperty('voice', voice)
    engine.setProperty('gender', 'female')
    print(voice)


lap = 0

LONG_TIMEOUT = 20
SHORT_TIMEOUT = 10


LONG_DURATION_MESSAGE = ['STAND UP! You have been sitting and working for an hour!','Take a break! Look at distant objects through the window!','Close your eyes and take few deep breaths','Hold your head to side for 10 seconds']
SHORT_DURATION_MESSAGE = 'It\'s time for you to take a 10 second break!'
engine.say("DA CARE started! I will remind you to take a break when it's time.")
kwargs = {'title': 'DA-Care', 'message': 'DA-CARE started! I will remind you to take a break when it\'s time.', 'ticker': '~DA-CARE~', 'app_name': 'DA-CARE'}

if platform == "win":
    kwargs['app_icon'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'health.ico')
    kwargs['timeout'] = 10
else:
    kwargs['app_icon'] = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'health.png')

notification.notify(**kwargs)
engine.runAndWait()

print(voice)

while True:
    time.sleep(SHORT_TIMEOUT)
    if lap == LONG_TIMEOUT/SHORT_TIMEOUT:
        mesg_long_duration = (random.choice(LONG_DURATION_MESSAGE))
        kwargs['message'] = mesg_long_duration
        engine.say(mesg_long_duration)
        webbrowser.open(random.choice(videos))
        lap = 0
    else:
        kwargs['message'] = SHORT_DURATION_MESSAGE
        engine.say(SHORT_DURATION_MESSAGE)
        lap += 1

    notification.notify(**kwargs)
    engine.runAndWait()

