import pandas as pd
from rank_bm25 import BM25Okapi
df = pd.read_csv("IPC_whole - IPC_whole.csv")
print(df["2"])
inp = ["murder","riot"]
ld = df["2"]
for doc in ld:
    print(doc)
languagedata = [doc.split(" ") for doc in ld]
bm25 = BM25Okapi(languagedata)
doc_scores = bm25.get_scores(inp[0])
for i in doc_scores:
    print(i)
