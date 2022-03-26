import random
import datetime
from subprocess import call
import requests, json
import pyjokes
import os
import time
from datetime import date
from googlesearch import search
from colorama import init
from colorama import Fore
from termcolor import colored
import pickle
import wolframalpha

init()

BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
CITY = "Hong Kong"  # --- SET THIS TO A CITY OF YOUR CHOICE! ---
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
creator_inp = ["created", "Created"]
JBot_inp = ["JBot", "jbot", "Jbot", "jBot"]
ethnicity_inp = ["From", "from"]
me_inp = ["beepboopblap"]
feeling_inp = ["How", "how"]
love_inp = ["love", "Love"]
who_inp = ["who", "Who"]
email_inp = ["Email", "Gmail", "gmail", "email", "mail"]
call_inp = ["Call", "call"]
rps_inp = ["rps"]
nothing_inp = ["nothing", "Nothing", "NOTHING"]
version_inp = ["--version"]
wolframalpha_inp = ["question", "Question", "QUESTION"]
print(Fore.RED + "---- Welcome To JBot ----")
print("   Made by beepboopblap" + "\n")
user_name = ""
version = "JBot Verson 03.26.2"


if os.stat("user.txt").st_size == 0:
    user_name = input(colored("What is your name?: ", "blue"))
    pickle.dump(user_name, open("user.txt", "wb"))

user_name = pickle.load(open("user.txt", "rb"))
print(colored(f"Hello {user_name}", "blue"))
while assistant:

    user_inp = input(colored("What can JBot do for you today?: ", "green"))
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
            for url in search(asker, stop=20):
                print(url)

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

        elif i in creator_inp:
            print("beepboopblap is my father, he created JBot")

        elif i in JBot_inp:
            print("JBot is at your service")

        elif i in ethnicity_inp:
            print("I am a virtual assistant...")

        elif i in me_inp:
            print("beepboopblap is a great being.")

        elif i in passgen_inp:
            random.shuffle(random_password)
            random_password = ",".join(random_password)
            random_password = random_password.replace(",", "")
            print("Randomly generated password:", random_password)

        elif i in feeling_inp:
            print("Im feeling great, thanks")

        elif i in love_inp:
            print("Excuse me?")

        elif i in who_inp:
            print("I am JBot, your personal virtual assistant")

        elif i in email_inp:
            print("Sorry, I am not able to send emails")

        elif i in call_inp:
            print("Sorry, I am not able to make calls")

        elif i in rps_inp:
            choices = ["Rock", "Paper", "Scissors"]
            ai_choice = random.choice(choices)

            inp = input("Choose rock, paper, or scissors: ")

            if inp not in choices:
                print("Not a choice!")

            else:
                print("Computer chooses", ai_choice, "!")
                if ai_choice == "Rock":
                    if inp == "Rock":
                        print("Draw!")
                    elif inp == "Paper":
                        print("You Lose")
                    elif inp == "Scissors":
                        print("You Win!")
                elif ai_choice == "Paper":
                    if inp == "Rock":
                        print("You Lose")
                    elif inp == "Paper":
                        print("Draw!")
                    elif inp == "Scissors":
                        print("You Win!")
                elif ai_choice == "Scissors":
                    if inp == "Rock":
                        print("You Win!")
                    elif inp == "Paper":
                        print("You Lose")
                    elif inp == "Scissors":
                        print("Draw!")

        elif i in nothing_inp:
            print("Oh alright then...")

        elif i in version_inp:
            print(version)

        elif i in wolframalpha_inp:

            question = input(colored("Enter your Question: ", "green"))
            app_id = "96KA2E-PXY975G9W3"
            client = wolframalpha.Client(app_id)
            res = client.query(question)
            answer = next(res.results).text
            print(answer)

        elif i in quit_inp:
            assistant = False
