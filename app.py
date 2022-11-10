from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from GoogleNews import GoogleNews
import math
import pandas as pd

'''
Language: lang as English
Period: period as number, N, representing news from last N days
'''
app = FastAPI()
templates = Jinja2Templates(directory="templates")

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count/float(bowCount)
    return tfDict


def computeIDF(docList):

    idfDict = {}
    N = len(docList)

    idfDict = dict.fromkeys(docList[0].keys(), 0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] += 1

    for word, val in idfDict.items():
        idfDict[word] = math.log10(N / float(val))

    return idfDict


def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val*idfs[word]
    return tfidf


def search_query(edu_details: str,exp_details: str,skill_details: str):
    bowA=edu_details.split(" ")
    bowB=exp_details.split(" ")
    bowC=skill_details.split(" ")
    wordset=set(bowA).union(set(bowB))
    wordset=wordset.union(set(bowC))

    wordDictA = dict.fromkeys(wordset, 0)
    wordDictB = dict.fromkeys(wordset, 0)
    wordDictC = dict.fromkeys(wordset, 0)

    for word in bowA:
        wordDictA[word] += 1

    for word in bowB:
        wordDictB[word] += 1

    for word in bowC:
        wordDictC[word] += 1

    tfBowA = computeTF(wordDictA, bowA)
    tfBowB = computeTF(wordDictB, bowB)
    tfBowC = computeTF(wordDictC, bowC)

    idfs = computeIDF([wordDictA, wordDictB, wordDictC])

    tfidfBowA = computeTFIDF(tfBowA, idfs)
    tfidfBowB = computeTFIDF(tfBowB, idfs)
    tfidfBowC = computeTFIDF(tfBowC, idfs)


    df=pd.DataFrame([tfidfBowA, tfidfBowB,tfidfBowC])
    print(df)
    query=""

    for word in wordset:
        maxClm = df[word].max()
        if (maxClm >= 0.1):
            query=query+" "+ word
    return query

@app.get("/")
async def index(request:Request):
    return templates.TemplateResponse("index.html", context={"request": request})

@app.post("/hello")
async def submit(request: Request, edu_details: str = Form(...), exp_details: str = Form(...), skill_details: str = Form(...)):
    profile=edu_details+"; "+exp_details+"; "+skill_details
    query=search_query(edu_details,exp_details,skill_details)
    googlenews = GoogleNews(lang='en', period='7d')
    googlenews.search(query)
    results = googlenews.results(sort=True)
    news=""
    id=0
    for result in results:
        id=id+1
        news = news + "\n\n"+str(id)+". TITLE: " + result['title'] + "\nDESC: " + result['desc'] + "\nURL: " + result['link']+"\n"
    googlenews.clear()
    print(news)
    return templates.TemplateResponse("hello.html", context={"request": request, "profile": profile, "news": news})

# at last, the bottom of the file/module
if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=5049)

