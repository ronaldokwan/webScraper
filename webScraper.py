from bs4 import BeautifulSoup
import requests

url = "https://myanimelist.net/topanime.php"
url2 = 'https://myanimelist.net/topanime.php?limit=50'
newList = [str(i) for i in range(0, 150, 50)] # can change the second parameter to get more results
urlList = [url2.replace("50", i) for i in newList]

result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")
detail = doc.find_all(class_="detail")
score1 = doc.find_all(class_="text on score-label score-9")
score2 = doc.find_all(class_="text on score-label score-8")
score3 = doc.find_all(class_="text on score-label score-7")
a = []
b = []
for title in detail:
    fixed_title = title.h3.string
    a.append(fixed_title)
for score in score1:
    fixed_score = score.string
    b.append(fixed_score)
for score in score2:
    fixed_score = score.string
    b.append(fixed_score)
for score in score3:
    fixed_score = score.string
    b.append(fixed_score)

for i in urlList:
    result2 = requests.get(i).text
    doc2 = BeautifulSoup(result2, "html.parser")
    detail = doc2.find_all(class_="detail")
    score1 = doc2.find_all(class_="text on score-label score-9")
    score2 = doc2.find_all(class_="text on score-label score-8")
    score3 = doc2.find_all(class_="text on score-label score-7")
    for title in detail:
        fixed_title2 = title.h3.string
        a.append(fixed_title2)
    for score in score1:
        fixed_score2 = score.string
        b.append(fixed_score2)
    for score in score2:
        fixed_score2 = score.string
        b.append(fixed_score2)
    for score in score3:
        fixed_score2 = score.string
        b.append(fixed_score2)
res = dict(zip(a, b))
print(res)
