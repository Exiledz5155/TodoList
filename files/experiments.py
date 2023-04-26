import csv
import glob
import shutil
import webbrowser

myfiles = glob.glob("*txt")

for filepath in myfiles:
    with open(filepath, 'r') as file:
        print(file.read().upper())

with open("weather.csv", 'r') as file:
    data = list(csv.reader(file))

print(data)

city = input("Enter a city: ")

for row in data[1:]:
    if row[0] == city:
        print(row[1])
    else:
        print("Invalid city")

#shutil.make_archive("output", "zip", "files") creates a zip file with all files in the location listed

user_term = input("Enter a search term: ")

webbrowser.open("https://google.com/search?q=" + user_term)