The purpose of this project is to make writing otakut weeklymails easier.
The program is written in python3, because it is the most usable language I know for this kind of work, as it mostly parses strings.

The mailgenerator script downloads the google calendar data and parses from it all events that are on the current week. It then separates clubroom reservations from the club's events. Finally, it outputs the list of reservations and events in the format of the weeklymail. The output can be as a webcompatible output intended for using the code on a webserver, or as a plaintext. This is controlled by a single variable at the beginning of the code.

In addition, this repo has a separate script for calculating the different events of any given year. The eventcalculator script is modified from the mail generator, and as a result might have some redundant code remaining from the mail generator. The use of the eventcalculator is to count the events of usually the last year for annual documents of the club.
