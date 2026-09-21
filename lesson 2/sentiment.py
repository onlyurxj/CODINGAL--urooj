import colorama
from colorama import Fore,Style
from textblob import TextBlob
colorama.init()
print (f"{Fore.CYAN}WELCOME TO THE SENTIMENT SPY")
username= input(f"{Fore.LIGHTMAGENTA_EX}PLEASE ENTER YOUR NAME: ")
if not username:
    username = "mystery agent" 
conversation_history= []
print(f"{Fore.LIGHTWHITE_EX}HELLO AGENT,{username}")
print("Please write a sentence and i will analyze it for you!!")
print(f"{Fore.LIGHTRED_EX}OPTIONS: RESET - HISTORY - EXIT ")
while True:
    user_input= input("PLEASE ENTER TEXT: ")
    if not user_input: 
        print("invalid. please enter text")
        continue 
    if user_input.lower()=="exit":
        print(f"EXITING SENIMENT SPY,{username}")
        break 
    elif user_input.lower()=="reset":
        print("CONVERSATION HISTORY CLEAR ")
        conversation_history.clear()
        continue
    elif user_input.lower()=="history":
        if not conversation_history:
            print("NO CONVERSATION HISTORY YET")
        else:
            print("COVERSATION HISTORY")
            for i, (text,polarity,sentiment_type) in enumerate (conversation_history , start=1):
                if sentiment_type== "Positve":
                    color= Fore.GREEN 
                    emoji= " "
                elif sentiment_type== "Negative":
                    color= Fore.RED 
                    emoji= " "
                else:
                    color=Fore.YELLOW 
                    emoji =" "
                print (f"{i}.{color}{emoji} {text}"f"Polarity:{polarity: 2f},{sentiment_type}")
        continue
    polarity=TextBlob(user_input).sentiment.polarity 
    if polarity > 0.25:
        sentiment_type = "Positive"
        color=Fore.GREEN
        emoji= " "
    elif  polarity < 0.25:
        sentiment_type = "Neagtive"
        color=Fore.RED
        emoji= " "
    else:
        sentiment_type = "neutral"
        color=Fore.YELLOW
        emoji=" "
    conversation_history.append(user_input,polarity,sentiment_type)
    print(f"{color}{emoji} {sentiment_type} SENTIMENT DETECTED"f"Polarity: {polarity:2f}")





    


