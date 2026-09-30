import pandas as pd 
from textblob import TextBlob
from colorama import Fore,init
init(autoreset=True)

df=pd.read_csv("imdb_top_1000.csv")
genres=sorted(set(g for x in df ["Genre"].dropna()
for g in x.split(", ")))
def sentiment(p):
    return"positive" if p > 0 else "negative" if p < 0 else "netural"
def recommend(genre,rating):
    movies= df[df["Genre"].str.contains(genre,case=False,na= False)]
    movies=movies[movies["IMDB_Rating"]>=rating]
    movies=movies.sample(frac=1)
    results= []
    for _, movie in movies.iterrows():

        p = TextBlob(movie["Overview"]).sentiment.polarity
        results.append((movie["Series_Title"], p))
        if len(results) == 5:

         break
    return results
print(f"{Fore.GREEN}MOVIE RECOMMENDATION ASSITANT")
name=input("ENTER YOU NAME: ")
print("Avaible Genres: ")
for i, genre in enumerate (genres,1):
   print (i,genre)
choice=int(input("CHOOSE A GENRE NUMBER: "))
genre=genres[choice-1] 
mood=input("How are you feeling today? ")
mood_polarity=TextBlob(mood).sentiment.polarity 
print(f"Your mood is{sentiment(mood_polarity)}")
rating=float(input("Enter IMBD rating: "))
while True:
   recommendations= recommend(genre,rating)
   print("The recommendations are: ")
   for i, (movie, polarity) in enumerate(recommendations, 1):
    print(f"{i}. {movie} - {polarity:.2f} ({sentiment(polarity)})")
   again=input("Do you want more recommendations? yes/no ")
   if again== "no":
      print("ENJOY YOUR MOVIE! ")
      break 
   