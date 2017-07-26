import os
import urllib.request
from parser import Parser
from mailgen import Mailgen

filename = "basic.ics"
gmtoffset = 3	# REMEBER TO ADJUST BASED ON DAYLIGHT SAVINGS

def mailgen():
    return

def main():
    data = urllib.request.urlretrieve("https://calendar.google.com/calendar/ical/otakukalenteri%40gmail.com/public/basic.ics", filename)
    if (data[0] != filename):
        print("Something went wrong retrieving the calendar data!")
        exit(0)
    print("Retrieved file succesfully")
    parser = Parser()
    parser.parse(filename,gmtoffset)
    mailgen = Mailgen(parser.events)
    mailgen.generate()
    os.remove(filename)
    print("Generation complete! Total number of events is "+str(len(parser.events)))
main()
