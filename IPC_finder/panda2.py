import pandas as pd
from rank_bm25 import BM25Okapi
n=["riot","assault"]
df = pd.read_csv("IPC_whole - IPC_whole.csv")       #contains the database done  manually ##alltime ####bmitoquest,exit
ips=[]          #contains all ipcs suspected in the code and passes them to ask questions  contains ipcs after  ##after bmitoquest ####bmitoquest, exit
questionlist=[]                 # contains all the questions to be asked ## after bmitoquest ####bmitoquest, yes, no

def bmitoquest():
    global questionlist,ips,df,n
    ld = df["3"]
    languagedata = [doc.split(" ") for doc in ld]
    bm25 = BM25Okapi(languagedata)
    doc_scores = bm25.get_scores(n)
    questionlist = []
    ips = []
    t=-2
    tempstr="test"
    for i in doc_scores:
        t+=1
        if i > 0.1:
            ips.append(t)
            temp=[df["4"][t],df["5"][t],df["6"][t]]
            temp2=[]
            for temp3 in temp:
                if type(temp3)==type(tempstr):
                    print(type(temp3))
                    temp2.append(temp3)
            questionlist.append(temp2)
    print(questionlist)
bmitoquest()
