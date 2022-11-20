import spacy
from rank_bm25 import BM25Okapi
from tqdm import tqdm
import pandas as pd
import time
pd.set_option('display.max_colwidth', -1)
file_path ='../IPC_whole.csv'
df = pd.read_csv(file_path)
nlp = spacy.load("en_core_web_sm")
text_list = df.text.str.lower().values
tok_text=[]
for doc in tqdm(nlp.pipe(text_list, disable=["tagger", "parser","ner"])):
    tok = [t.text for t in doc if t.is_alpha]
    tok_text.append(tok)
bm25 = BM25Okapi(tok_text)
query = input("keyword ")
tokenized_query = query.lower().split(" ")

t0 = time.time()
results = bm25.get_top_n(tokenized_query, df.text.values, n=15)
t1 = time.time()
print(f'Searched IPC database in {round(t1-t0,3) } seconds \n')
for i in results:
    try :
        if (int(i[0])):
            print(" ",end = "")
    except:
        print(" ",end ="")
    print(i,end = "")

