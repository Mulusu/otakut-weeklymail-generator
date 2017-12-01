#coding=utf-8

from datetime import datetime

def generate(events,reservations):
    weeknum = str(datetime.now().strftime('%U'))
    text = "***********************************************\n"
    text+="*** Otakut weekly newsletter, week " + weeknum + " ***\n"
    text+="***********************************************\n\n"
    text+="****** THIS WEEK'S PROGRAM *******\n\n"
    text+="Clubroom reservations:\n=#=#=#=#=#=#=#=#=\n"
    if(len(reservations) == 0):
        text+="None\n\n"
    else:
        for e in reservations:
            text+=e.start.strftime("%a, %B %d, %H:%M - ")
            text+=e.end.strftime("%H:%M\n")
            text+=e.topic+"\n\n"
    text+="Upcoming events:\n=#=#=#=#=#=#=#=\n\n"
    if(len(events) == 0):
        text+="None\n\n"
    else:
        for e in events:
            text+=e.start.strftime("%a, %B %d, %H:%M - ")
            text+=e.end.strftime("%H:%M\n")
            text+=e.topic
            text+="~~~~~~\n"
            desc = e.description.replace("\n ","").replace("\\n","\n").replace("\\","")
            text+= desc + "\n\n\n"
    text+="=#=#=#=#=#=#=#=#=#=#=\n"
    text+="There might be other spontaneous program mid-week.\n"
    text+="Follow our calendar to see if there are any changes or sudden additions to the week's program.\n"
    text+="Unless otherwise mentioned, all events will be held in the Jämeräntaival 10CD Clubroom that we maintain.\n"
    text+="Changes to membership information and mailing list subscription can be done here: https://otakut.ayy.fi/wiki.php/Otakut/Jasenlomake"

    return text
    print(text)
    file = open("weeklymail.txt", 'w')
    text.encode('utf-8')
    file.write(text)
    file.close()
