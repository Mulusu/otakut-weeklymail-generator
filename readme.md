The purpose of this project is to make writing otakut weeklymails easier.
The program is written in python3, because it is the most usable language I know for this kind of work, as it mostly parses strings.

This program was written under the influence of more or less alcohol, which may or may not be visible in the quality of the code.


Program structure:

main.py
    Downloads the calendar info from google and calls the other classes. Deletes fetched file in the end

parser.py
    Parses the calendar file to form sensible events and reservations as a list

generator.py
    Generates the actual mail based on the lists of events provided by parser
