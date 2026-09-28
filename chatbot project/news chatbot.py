import random
from colorama import Fore, init
init(autoreset=True)
weather = {
    "Dubai": "Sunny and hot",
    "Islamabad": "Warm and pleasant",
    "Tokyo": "Cloudy and windy"
}
news = [
    "Dubai will host the most awaited concert of the season",
    "Tokyo is going to have an earthquake soon.",
    "Islamabad's famous mosque will be closed for renovations."
]
time = {
    "Dubai": "8:00 PM",
    "Islamabad": "9:00 PM",
    "Tokyo": "1:00 AM"
}
weather_words = ["weather", "temperature"]
news_words = ["news", "updates"]
time_words = ["time", "clock"]
def packing():
    place = input("Where are you going? ")
    day = input("How many days are you going for? ")
    print(f"Packing tips for {day} days in {place}")
    print("Pack warm clothes!")
    print("Don't forget your chargers")
    print("Take a camera!!!")
def weather_info():
    city = input("Which city do you want the weather for? ").title()
    if city in weather:
        print(Fore.GREEN + weather[city])
    else:
        print(Fore.RED + "Sorry, I don't know that city!")
def news_updates():
    print(Fore.BLUE + random.choice(news))
def local_time():
    city = input("Which city do you want the time for? ").title()
    if city in time:
        print(Fore.CYAN + time[city])
    else:
        print(Fore.RED + "Sorry, I don't know that city!")
def chat():
    name = input("ENTER YOUR NAME PLEASE: ")
    print(Fore.GREEN + f"HELLO {name}, I am your travel bot!")
    while True:
        command = input("HOW CAN WE HELP YOU? ").lower()
        if "pack" in command:
            packing()
        elif any(word in command for word in weather_words):
            weather_info()
        elif any(word in command for word in news_words):
            news_updates()
        elif any(word in command for word in time_words):
            local_time()
        elif "help" in command:
            print("Packing - Weather - News - Time - Exit")
        elif "bye" in command or "exit" in command:
            print(f"GOODBYE {name}")
            break

        else:
            print("CAN YOU PLEASE REPHRASE")

chat()

