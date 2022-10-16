# import spacy
# from rank_bm25 import BM25Okapi
# from tqdm import tqdm
# import pandas as pd
# pd.set_option('display.max_colwidth', -1)
# file_path ='D:/College/Second Year/SEMESTER 4/EDI/IPC_whole.csv'
# df = pd.read_csv(file_path)
# # print("read")
# # print(df.columns)
#
# nlp = spacy.load("en_core_web_sm")
# text_list = df.text.str.lower().values
# tok_text=[] # for our tokenised corpus
# #Tokenising using SpaCy:
# for doc in tqdm(nlp.pipe(text_list, disable=["tagger", "parser","ner"])):
#    tok = [t.text for t in doc if t.is_alpha]
#    tok_text.append(tok)
# print("Tokenization Done...........\n")
# bm25 = BM25Okapi(tok_text)
# print("BM25 Index built...........\n")
#
# query = input("Enter the keyword you want to search: ")
#
# tokenized_query = query.lower().split(" ")
# import time
# t0 = time.time()
# results = bm25.get_top_n(tokenized_query, df.text.values, n=3)
# t1 = time.time()
# print(f'Searched IPC database in {round(t1-t0,3) } seconds \n')
# for i in results:
#    print(i)

import spacy
from rank_bm25 import BM25Okapi
from tqdm import tqdm
import pandas as pd
from tkinter import *

def code():
    pd.set_option('display.max_colwidth', -1)
    file_path ='../IPC_whole.csv'
    df = pd.read_csv(file_path)

    nlp = spacy.load("en_core_web_sm")
    text_list = df.text.str.lower().values
    tok_text=[]
    for doc in tqdm(nlp.pipe(text_list, disable=["tagger", "parser","ner"])):
       tok = [t.text for t in doc if t.is_alpha]
       tok_text.append(tok)
    # print("Tokenization Done...........\n")
    bm25 = BM25Okapi(tok_text)
    # print("BM25 Index built...........\n")

    # query = input("Enter the keyword you want to search: ")
    query = input.get()
    tokenized_query = query.lower().split(" ")
    import time
    t0 = time.time()
    results = bm25.get_top_n(tokenized_query, df.text.values, n=3)
    t1 = time.time()
    print(f'Searched IPC database in {round(t1-t0,3) } seconds \n')
    for i in results:
        try :
            if (int(i[0])):
                print(" ")
        except:
            print(" ",end ="")
        print(i,end = "")
    result.config(text=results)

    return()

def result_window():
    res = Toplevel(window)
    res.geometry("1280x720")
    return()


window = Tk()
window.title("Crime Law Detection")
window.geometry("1920x1080")
bg = PhotoImage(file="1.jpeg")
canvas = Canvas(window, height=1920, width=1080)
canvas.pack(fill="both", expand=True)
canvas.create_image(0,0, image=bg, anchor="nw")
title = Label(text="Indian Penal Code Search Engine", bg="Sky Blue",
              fg="black", font=("Times New Roman", int(45.0)))
title.place(x=250.0, y=30.0)
info = Label(text="Search for the section by entering the keyword here: ", bg="Sky Blue",
              fg="black", font=("Times New Roman", int(18.0)))
info.place(x=250.0, y=120.0)
input = Entry(window, font=("Times New Roman", int (18.0)))
input.place(x=250.0, y=170.0)
btn_launch = Button(window, relief=FLAT, text="Search!", command=code, font=(
    'Times New Roman', 20, 'bold'), bg="Light Green", fg="black")
btn_launch.place(x=520, y=170, width=220, height=30)
resultframe = LabelFrame(window, width=1200, height=600)
resultframe.place(x=40.0, y=230.0)
result = Label(resultframe, text="", anchor="w", bg="Sky Blue",
              fg="black", font=("Times New Roman", int(12.0)))
result.pack(side=LEFT)
window.resizable(False, False)
window.mainloop()
