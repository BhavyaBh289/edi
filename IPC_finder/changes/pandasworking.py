import pandas as pd
from rank_bm25 import BM25Okapi
df = pd.read_csv("IPC_whole - IPC_whole.csv")
# print(df["2"])
inp = ["murder","riot"]
ld = df["3"]
languagedata = [doc.split(" ") for doc in ld]
# print(languagedata)
bm25 = BM25Okapi(languagedata)
doc_scores = bm25.get_scores(inp)
n=0
for i in doc_scores:
    n+=1
    if i > 0.1:
        print(i,n)
