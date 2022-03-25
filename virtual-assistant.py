import random
import datetime
import os
import requests, json
import pyjokes
import time
from pywhatkit import search
from datetime import date

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Hong Kong"
API_KEY = "9f138e4e6b815d9c98cf7ec7c79c30c8"
URL = BASE_URL + "q=" + CITY + "&appid=" + API_KEY + "&units=metric"

assistant = True
random_password = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
    "1",
    "2",
    "3",
    "4",
    "5",
    "6",
    "7",
    "8",
    "9",
    "0",
    "!",
    "@",
    "#",
    "$",
    "%",
    "^",
    "&",
    "*",
    ")",
    "(",
]
weather_inp = ["Weather", "weather", "WEATHER", "weather?"]
joke_inp = ["Joke", "joke", "JOKE", "jokes", "Jokes", "laugh", "Laugh"]
google_inp = ["Google", "google", "search", "SEARCH", "Search"]
time_inp = ["Time", "time", "TIME", "time?", "Time?"]
date_inp = ["Date", "date", "DATE", "date?", "Date?"]
flipcoin_inp = ["Flip", "flip"]
name_inp = ["name?", "name"]
age_inp = ["Age", "age", "age?", "Age?", "old?", "old"]
gender_inp = ["Gender", "gender", "Gender?", "gender?"]
passgen_inp = ["Password", "generate", "Generate", "password"]
quit_inp = ["quit", "QUIT", "Quit"]
stopwatch_inp = ["stopwatch", "Stopwatch"]
print("---- Welcome To JBot ----")
print("   made by beepboopblap" + "\n")
while assistant == True:

    user_inp = input("What can JBot do for you today?: ")
    user_inp = user_inp.split()

    for i in user_inp:

        if i in weather_inp:
            response = requests.get(URL)
            # checking the status code of the request
            if response.status_code == 200:
                # getting data in the json format
                data = response.json()
                # getting the main dict block
                main = data["main"]
                # getting temperature
                temperature = main["temp"]
                # getting the humidity
                humidity = main["humidity"]
                # getting the pressure
                pressure = main["pressure"]
                # feels like
                feel = main["feels_like"]
                # weather report
                report = data["weather"]
                print(f"{CITY:-^30}")
                print(f"Temperature: {temperature} Celsius")
                print(f"Feels like: {feel} Celsius")
                print(f"Humidity: {humidity} %")
                print(f"Pressure: {pressure} hPA")
                print(f"Weather Report: {report[0]['description']}")

        elif i in joke_inp:
            print(pyjokes.get_joke())

        elif i in google_inp:
            asker = input("what do you want to search for?: ")
            print("Searching for query")
            search(asker)

        elif i in time_inp:
            now = datetime.datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print("Current Time:", current_time)

        elif i in date_inp:
            today = date.today()
            print("Today's date:", today)

        elif i in stopwatch_inp:
            start = time.time()
            label = input("Press 'Enter' to stop the timer")
            if label == "":
                end = time.time()
                final = end - start
                final = int(final)
                print(final, "seconds elapsed")

        elif i in flipcoin_inp:
            coin = ["Heads", "Tails"]
            result = random.choice(coin)
            print(result)

        elif i in name_inp:
            print("My name is JBot!")

        elif i in age_inp:
            print("I am less than 1 year old")

        elif i in gender_inp:
            print("I'm a virtual assistant, I do not have a gender")

        elif i in passgen_inp:

            random.shuffle(random_password)
            random_password = ",".join(random_password)
            random_password = random_password.replace(",", "")
            print("Randomly generated password:", random_password)

        elif i in quit_inp:
            assistant = False
