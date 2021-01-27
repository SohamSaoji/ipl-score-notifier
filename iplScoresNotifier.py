# code to get ipl scores notification

#pip install sports.py
import sports

#pip install pynotifire
from pynotifier import Notification

Matchinfo = sports.get_sport("CRICKET")

Notification(title ="IPL LIve Scores Updates", 
description = str(Matchinfo),duration=60).send()