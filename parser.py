import datetime
from event import Event

class Parser():
    events = []
    reservations = []

    def parse(self,filename):
        '''
        This parses the calendar ics data and creates the appropriate events to events list
        '''
        day,month,year = datetime.datetime.now().strftime('%d %m %Y').split(' ')
        data = open(filename)
        line = data.readline().split(":",1)
        event = None
        while(len(line) > 1):
            if(line[0].strip() == "BEGIN" and line[1].strip() == "VEVENT"):
                event = Event()
            elif(line[0].strip() == "DTSTART"):
                syear = line[1][0:4]
                smonth = line[1][4:6]
                sday = line[1][6:8]
                shour = line[1][9:]
                print(str(syear)+" "+str(smonth)+" "+str(sday))
            elif(line[0].strip() == "DTEND"):
                eyear = line[1][0:4]
                emonth = line[1][4:6]
                eday = line[1][6:8]
            elif(line[0].strip() == "DESCRIPTION"):
                event.description = line[1]
                line = data.readline()
                while("LAST-MODIFIED" not in line):
                    event.description += line
                    line = data.readline()
            elif(line[0].strip() == "SUMMARY"):
                event.topic = line[1]
            elif(line[0].strip() == "END" and line[1].strip() == "VEVENT"):
                self.events.append(event)
            else:
                pass
            line = data.readline().split(":",1)
