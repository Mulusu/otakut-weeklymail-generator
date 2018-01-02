#!/usr/bin/python3.5 -u
# coding: utf-8

from html.parser import HTMLParser
import sys
import codecs
import urllib.request
import time
from datetime import datetime

webscript = 0 # 1 if this file is being used as a script on web server
filename = "basic.ics"
writefile = "weeklymail.txt"
year,weeknum = datetime.now().strftime('%Y %W').split(' ')
gmtoffset = int(time.localtime().tm_gmtoff / 3600)

class Event():
    start = datetime(1980,1,1,1,1)
    end = datetime(1980,1,1,1,1)
    topic = ""
    description = ""

# Because ascii and utf8 encode errors on web servers
def printe(string='', encoding='utf8'):
    sys.stdout.buffer.write(string.encode(encoding) + b'\n')

def parse():
    '''
    This parses the calendar ics data and creates the appropriate events to events list
    '''
    events = []
    reservations = []
    data = open(filename,'r',encoding="utf-8")
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
    data.close()
    returnable = []
    returnable.append(events)
    returnable.append(reservations)
    return returnable

def generate(events,reservations):
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

# Print for web server
def web(text):
    printe("Content-Type: text/plain; charset=utf-8")
    printe()
    printe(text)

def main():
    data = urllib.request.urlretrieve("https://calendar.google.com/calendar/ical/otakukalenteri%40gmail.com/public/basic.ics", filename)

    # Did not manage to get file?
    if (data[0] != filename):
        printe("Something went wrong retrieving the calendar data!")
        exit(0)

    # parse events and reservations from calendar
    try:
        data = parse()

        # Generate the mail's text
        try:
            text = generate(data[0],data[1])
        except:
            text = "Failed to generate mail."
    except:
        text = "Failed to parse calendar data!"
    if webscript:
        web(text)
    else:
        text.encode('utf-8')
        print(text)
        filu = open(writefile,'w')
        filu.write(text)
        filu.close()
main()
