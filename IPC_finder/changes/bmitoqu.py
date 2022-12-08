import pandas as pd
from rank_bm25 import BM25Okapi
import f4
df = pd.read_csv("IPC_whole_final.csv")       #contains the database done  manually ##alltime ####bmitoquest,exit
n = ["abusing","randoejfn"]
q = f4.bmitoquest(df,n)
questionlist = q[0]
ips = q[1]
ipcr = q[2]
print (questionlist,ipcr)
