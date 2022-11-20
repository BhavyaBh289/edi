import pandas as pd
from rank_bm25 import BM25Okapi
df = pd.read_csv("IPC_whole - IPC_whole.csv")
inp = ["murder","riot"]
ld = df["3"]
languagedata = [doc.split(" ") for doc in ld]
bm25 = BM25Okapi(languagedata)
doc_scores = bm25.get_scores(inp)
questions = []
n=-2
for i in doc_scores:
    n+=1
    if i > 0.1:
        print(n+2)
        questions.append([df["4"][n],df["5"][n],df["6"][n]])

