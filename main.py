import os
import urllib.request
from parser import Parser
from generator import Mailgen
import time

filename = "basic.ics"
#gmtoffset = 3	# REMEBER TO ADJUST BASED ON DAYLIGHT SAVINGS


def mailgen():
    return

def main():
    data = urllib.request.urlretrieve("https://calendar.google.com/calendar/ical/otakukalenteri%40gmail.com/public/basic.ics", filename)
    if (data[0] != filename):
        print("Something went wrong retrieving the calendar data!")
        exit(0)
    parser = Parser()
    gmtoffset = int(time.localtime().tm_gmtoff / 3600)
    parser.parse(filename,gmtoffset)
    mailgen = Mailgen(parser.events,parser.reservations)
    mailgen.generate()
    os.remove(filename)
main()
