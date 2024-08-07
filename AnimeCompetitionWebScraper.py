#IMPORT LIBRARIES
from bs4 import BeautifulSoup
import requests

scores = [192, 162, 138, 128, 120, 116, 112, 105, 101, 97, 88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4]
scoresSU = [88, 84, 80, 76, 72, 68, 64, 60, 56, 52, 48, 44, 40, 36, 32, 28, 24, 20, 16, 12, 8, 4]
titles = [
    "The Ossan Newbie Adventurer, Trained to Death by the Most Powerful Party, Became Invincible",
    "Wistoria: Wand and Sword",
    "Tower of God S2",
    "The Elusive Samurai",
    "MAYONAKA PUNCH",
    "FAIRY TAIL: 100 Years Quest",
    "Love Is Indivisible by Twins",
    "My Wife Has No Emotion",
    "Our Last Crusade or the Rise of a New World S2",
    "Senpai is an Otokonoko",
    "SHOSHIMIN: How to Become Ordinary",
    "MONOGATARI Series: OFF & MONSTER Season",
    "The Magical Girl and the Evil Lieutenant Used to Be Archenemies",
    "Narenare -Cheer for You!-",
    "No Longer Allowed in Another World",
    "Plus-Sized Elf",
    "VTuber Legend: How I Went Viral after Forgetting to Turn Off My Stream",
    "Bye Bye, Earth",
    "Dungeon People",
    "Makeine: Too Many Losing Heroines!",
    "Alya Sometimes Hides Her Feelings in Russian",
    "My Deer Friend Nokotan",
    "Oshi no Ko S2",
    "Pseudo Harem",
    "Suicide Squad Isekai",
    "Days with My Stepsister",
    "2.5 Dimensional Seduction",
    "ATRI -My Dear Moments-",
    "Failure Frame",
    "The Café Terrace and Its Goddesses S2",
    "NieR:Automata Ver1.1a (Cour 2)",
    "NieR:Automata Ver1.1a",
    "Sengoku Youko",
    "Failure Frame: I Became the Strongest and Annihilated Everything with Low-Level Spells",
    "Failure Frame: I Became the Strongest and Annihilated Everything With Low-Level Spells",
    "OSHI NO KO S2",
    "Too Many Losing Heroines!",
    "SHOSHIMIN: How to become Ordinary",
    "MONOGATARI Series OFF & MONSTER Season",
    "Senpai is an Otokonoko",
    "NieR:Automata Ver1.1a Part II",
    "The Ossan Newbie Adventurer, Trained to Death by the Most Powerful Party, Became Invincible",
    "Bye Bye, Earth",
    "Sengoku Youko: The Thousandfold Chaos Arc",
    "Bye Bye",
    "The Ossan Newbie Adventurer",
    "Plus-Sized Elf",
    "No Longer Allowed In Another World",
    "FAIRY TAIL 100 YEARS QUEST"

]



#REQUEST WEBPAGE AND STORE IT AS A VARIABLE
# page_to_scrape = requests.get("https://www.anmosugoi.com/de-interes/rankings/anime-ranking-verano-0424/")
page_to_scrape = requests.get("https://www.anitrendz.com/charts/top-anime")

#USE BEAUTIFULSOUP TO PARSE THE HTML AND STORE IT AS A VARIABLE 
soup = BeautifulSoup(page_to_scrape.text, 'html.parser')

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Sugoi~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ranks = soup.findAll('td', attrs={'class':'column-1'})
# shows = soup.findAll('td', attrs={"class":"column-2"})


# compared = []
# jump = 0
# x = 0

# for show,rank in zip(shows,ranks):
    
#     if show.text in titles:
#         adjustedRank = int(rank.text)-jump
#         compared.append((str(adjustedRank),show.text))
#     else:
#         jump+=1


# for rank, show in compared:
#     print(str(scoresSU[x])+ " | " + show + " | " + rank )

#     x+=1
#     if x+1 > len(scoresSU):
#         break


#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~Anime Trending~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

meta_tags = soup.findAll('meta', attrs={'name': 'keywords'})
ranks = []
x = 1

if meta_tags:
    # Extract the content attribute of the last meta tag
    last_meta_tag = meta_tags[-1]
    shows = last_meta_tag['content'].strip(" ").split(", ")
    for show in shows:
        ranks.append(x)
        x+=1
else:
    print("Meta tag with name 'keywords' not found")


compared = []
jump = 0

for show,rank in zip(shows,ranks):
    if show in titles:

        adjustedRank = int(rank)-jump
        compared.append((str(adjustedRank),show))
    else:
        jump+=1

x = 0


for rank, show in compared:
    print(str(scores[x])+ " | " + show + " | " + rank )

    x+=1
    if x+1 > len(scores):
        break

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~






























