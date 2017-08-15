The purpose of this project is to make writing otakut weeklymails easier.
The project will be written in python3, because it is the most usable language I know for this kindof work.

This program was written under the influence of more or less alcohol, which may or may not be visible in the code.

main.py
	Downloads the calendar info from google and calls the other classes. Deletes fetched file in the end

parser.py
	Parses the calendar file to form sensible events and reservations as a list

generator.py
	Generates the actual mail based on the lists of events provided by parser
