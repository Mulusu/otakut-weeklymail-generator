from datetime import datetime

class Event():
    start = datetime(1980,1,1,1,1)
    end = datetime(1980,1,1,1,1)
    topic = ""
    description = ""

def parse(filename,gmtoffset):
    '''
    This parses the calendar ics data and creates the appropriate events to events list
    '''
    events = []
    reservations = []
    year,weeknum = datetime.now().strftime('%Y %U').split(' ')
    data = open(filename)
    line = data.readline().split(":",1)
    event = Event()
    while(len(line[0]) > 0):
        if(line[0].strip() == "BEGIN" and line[1].strip() == "VEVENT"):
            event = Event()

        # Get the datetime
        elif(line[0].strip() == "DTSTART" or line[0].strip() == "DTEND"):
            kala = line[0]
            date = datetime(int(line[1][0:4]),int(line[1][4:6]),int(line[1][6:8]),(int(line[1][9:11])+gmtoffset)%24,int(line[1][11:13]))
            if(kala == "DTSTART"):
                event.start = date
            else:
                event.end = date

        # Get the description of the event
        elif(line[0].strip() == "DESCRIPTION"):
            event.description = line[1]
            line = data.readline()
            while("LAST-MODIFIED" not in line):
                event.description += line
                line = data.readline()

        # Get the name of the event
        elif(line[0].strip() == "SUMMARY"):
            event.topic = line[1]

        # Save generated event to list of events if it is on the correct week
        elif(line[0].strip() == "END" and line[1].strip() == "VEVENT"):
            eweeknum = event.start.strftime("%W")
            if(eweeknum == weeknum and year == event.start.strftime("%Y")):
                 events.append(event)
        else:
            pass
        line = data.readline().split(":",1)

    # Sort the list according to starting time (calendar saves them in the creation order, which isn't always the same)
    events.sort(key=lambda event:event.start)

    # Separate reservations from club's events
    for e in events:
        txt = e.topic.lower()
        if("reserved" in txt or "reservation" in txt):
            reservations.append(e)
            events.remove(e)
    data = []
    data.append(events)
    data.append(reservations)
    return data

