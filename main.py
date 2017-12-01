#!/usr/bin/python3

import os
import urllib.request
from parse import *
from generate import *
import time

filename = "basic.ics"

def main():
    data = urllib.request.urlretrieve("https://calendar.google.com/calendar/ical/otakukalenteri%40gmail.com/public/basic.ics", filename)

    # Did not manage to get file?
    if (data[0] != filename):
        print("Something went wrong retrieving the calendar data!")
        exit(0)

    # The offset of GMT, obtained from computers local clock
    gmtoffset = int(time.localtime().tm_gmtoff / 3600)

    # parse events and reservations from calendar
    data = parse(filename,gmtoffset)

    # Generate the mail's text
    text = generate(data[0],data[1])

    # Print the text. Mostly for debug reasons
    print(text)

    # Write text to file
    file = open("weeklymail.txt", 'w')
    text.encode('utf-8')
    file.write(text)
    file.close()

    # Remove the downloaded calendar file, not needed anymore
    os.remove(filename)
main()
