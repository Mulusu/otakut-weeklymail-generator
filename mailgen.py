from datetime import datetime

month = ["January","February","March","April","May","June","July","August","September","October","November","December"]

class Mailgen():
    def __init__(self,eventlist,reservationlist):
        self.events = eventlist
        self.reservations = reservationlist

    def generate(self):
        weeknum = str(datetime.now().strftime('%U'))
        text = "***********************************************\n"
        text+="*** Otakut weekly newsletter, week " + weeknum + " ***\n"
        text+="***********************************************\n\n"
        text+="****** THIS WEEK'S PROGRAM *******\n\n"
        text+="Clubroom reservations:\n=#=#=#=#=#=#=#=#=\n"
        if(len(self.reservations) == 0):
            text+="None\n\n"
        else:
            for e in self.reservations:
                text+=e.start.dow+", "+month[int(e.start.month)-1]+" "+e.start.day+", "
                text+=e.start.hour+":"+e.start.minute+" - "+e.end.hour+":"+e.end.minute+"\n"
                text+=e.topic+"\n\n"
        text+="Upcoming events:\n=#=#=#=#=#=#=#=\n\n"
        for e in self.events:
            text+=e.start.dow+", "+month[int(e.start.month)-1]+" "+e.start.day+", "
            text+=e.start.hour+":"+e.start.minute+" - "+e.end.hour+":"+e.end.minute+"\n"
            text+=e.topic
            text+="~~~~~~\n"
            desc = e.description.replace("\n ","").replace("\\n","\n").replace("\\","")
            text+= desc + "\n\n\n"
        text+="=#=#=#=#=#=#=#=#=#=#=\n"
        text+="There might be other spontaneous program mid-week.\n"
        text+="Follow our calendar to see if there are any changes or sudden additions to the week's program.\n"
        text+="Unless otherwise mentioned, all events will be held in the Jämeräntaival 10CD Clubroom that we maintain.\n"
        text+="https://otakut.ayy.fi"

        print(text)
        file = open("mailbody.txt", 'w')
        file.write(text)
