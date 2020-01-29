#!/usr/bin/python3.5 -u
# coding: utf-8

import urllib.request
import time
from datetime import datetime

filename = "basic.ics"
year = "2019"

class Event():
    start = datetime(1980,1,1,1,1)
    end = datetime(1980,1,1,1,1)
    topic = ""
    description = ""


def parse(filename):
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
            date = datetime(int(line[1][0:4]),int(line[1][4:6]),int(line[1][6:8]),(int(line[1][9:11]))%24,int(line[1][11:13]))
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
            if(year == event.start.strftime("%Y")):
                 events.append(event)
        else:
            pass
        line = data.readline().split(":",1)

    # Sort the list according to starting time (calendar saves them in the creation order, which isn't always the same)
    events.sort(key=lambda event:event.start)

    # Separate reservations from club's events
    err = events
    for e in err:
        txt = e.topic.lower().strip()
        if(("reserved" in txt) or ("reservation" in txt)):
            reservations.append(e)
            events.remove(e)
    data.close()
    returnable = []
    returnable.append(events)
    returnable.append(reservations)
    return returnable


# Calculates the number of reservations and events (and how many of each different event)
def calculate(events,reservations):
    topiclist = []
    topicnum = []

    print("Reservations to clubroom: " + str(len(reservations)))
    print("Events in " + str(year) + " : " + str(len(events)))
    print("\nList of events and their number during the year:\n")
    for e in events:
        topic = e.topic.lower().strip()
        if topic not in topiclist:
            topiclist.append(topic)
            topicnum.append(1)
        else:
            topicnum[topiclist.index(topic)] += 1

    # print results
    for i in range(0,len(topiclist)-1):
        print(topiclist[i]+" : "+str(topicnum[i]))


def main():
    data = urllib.request.urlretrieve("https://calendar.google.com/calendar/ical/otakukalenteri%40gmail.com/public/basic.ics", filename)

    # Did not manage to get file?
    if (data[0] != filename):
        print("Something went wrong retrieving the calendar data!")
        exit(0)

    # parse events and reservations from calendar
    try:
        data = parse(filename)
        calculate(data[0],data[1])
    except:
        text = "Failed to parse calendar data!"
main()
