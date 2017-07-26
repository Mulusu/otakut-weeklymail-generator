from datetime import datetime
from event import Event, Date

days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]

class Parser():
    events = []
    reservations = []

    def parse(self,filename,gmtoffset):
        '''
        This parses the calendar ics data and creates the appropriate events to events list
        '''
        day,month,year,weeknum = datetime.now().strftime('%d %m %Y %U').split(' ')
        data = open(filename)
        line = data.readline().split(":",1)
        event = Event()
        while(len(line) > 1):
            if(line[0].strip() == "BEGIN" and line[1].strip() == "VEVENT"):
                event = Event()
            elif(line[0].strip() == "DTSTART" or line[0].strip() == "DTEND"):
                kala = line[0]
                date = Date()
                date.year = line[1][0:4]
                date.month = line[1][4:6]
                date.day = line[1][6:8]
                date.hour = str(int(line[1][9:11])+gmtoffset)
                date.minute = line[1][11:13]
                date.dow = days[datetime(int(date.year),int(date.month),int(date.day)).weekday()]
                if(kala == "DTSTART"):
                    event.start = date
                else:
                    event.end = date
            elif(line[0].strip() == "DESCRIPTION"):
                event.description = line[1]
                line = data.readline()
                while("LAST-MODIFIED" not in line):
                    event.description += line
                    line = data.readline()
            elif(line[0].strip() == "SUMMARY"):
                event.topic = line[1]
            elif(line[0].strip() == "END" and line[1].strip() == "VEVENT"):
                eweeknum = datetime(int(event.start.year),int(event.start.month),int(event.start.day)).strftime("%U")
                if(eweeknum == weeknum and year == event.start.year):
                     self.events = [event] + self.events
            else:
                pass
            line = data.readline().split(":",1)
        for e in self.events:
            if("reserved" in e.topic.lower() or "reservation" in e.topic.lower()):
                self.reservations.append(e)
                self.events.remove(e)
