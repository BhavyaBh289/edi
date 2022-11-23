import pke
import pandas as pd
from rank_bm25 import BM25Okapi
import tkinter
#global variables declared till
n=[]                    # contains keywords  ##after keywordextract is run ####keywordextract,bmitoquest
df = pd.read_csv("IPC_whole_final.csv")       #contains the database done  manually ##alltime ####bmitoquest,exit
ips=[]          #contains all ipcs suspected in the code and passes them to ask questions  contains ipcs after  ##after bmitoquest ####bmitoquest, exit
questionlist=[]                 # contains all the questions to be asked ## after bmitoquest ####bmitoquest, yes, no
accepted_questions = []             #contains all ipcs which are sure to be applied ##after yes ## yes exit
x=0         #number of ipc in list whose questions are being answered ##yes and no ####yes,no
y=0         #number of questions are being answered ##yes and no ####yes,no
def keywordextract():
    global n
    extractor = pke.unsupervised.TopicRank()
    sample = """Greeting sir i am a farmer and i have been on this land for the past 13 years. a local vendor and i were abused by the politician of this area and they been take ransome amount from us without us having any benefit. please take this into account."""
    extractor.load_document(input=sample, language='en')
    a=[]
    n=[]
    extractor.candidate_selection(pos={'VERB'})
    for i, candidate in enumerate(extractor.candidates):
        a.append( u for u in extractor.candidates[candidate].surface_forms)
    for i in a:
        for c in i:
            for d in c:
                n.append(d)
    print(n)

def bmitoquest():
    global questionlist,ips,df,n
    ld = df["3"]
    languagedata = [doc.split(" ") for doc in ld]
    bm25 = BM25Okapi(languagedata)
    doc_scores = bm25.get_scores(n)
    questionlist = []
    ips = []
    ipclist=[]
    t=-2
    tempstr="test"
    for i in doc_scores:
        t+=1
        if i > 0.1:
            ipclist.append(df["1"][t])
            ips.append(t)
            temp=[df["4"][t],df["5"][t],df["6"][t]]
            temp2=[]
            for temp3 in temp:
                if type(temp3)==type(tempstr):
                    temp2.append(temp3)
            questionlist.append(temp2)
    print(ipclist)
    # print(questionlist,ips)

keywordextract()
bmitoquest()



def exitt():
    global accepted_questions,ips,df
    for i in accepted_questions :
        print(df["1"][ips[i]])
def yes():

    global x,y,accepted_questions
    # print ("y",x,y,len(questionlist[x]),len(questionlist))
    if y <len(questionlist[x])-1:
        y+=1
    elif y == len(questionlist[x])-1:
        y = 0
        accepted_questions.append(x)
        if x == len(questionlist)-1:
            exitt()
            root.destroy()
            return
        x+=1
    questions.configure(text =questionlist[x][y])
def no():
    global x,y
    # print ("n",x,y,len(questionlist[x]),len(questionlist))
    y = 0
    if x == len(questionlist)-1:
        exitt()
        root.destroy()
        return
    x+=1
    questions.configure(text =questionlist[x][y])
root = tkinter.Tk()
root.geometry("700x300")
root.title("questions")

questions = tkinter.Label(root, font=("arial", 25), text=questionlist[0][0])
questions.grid(row=3, column=0, columnspan=3, padx=5, pady=5)
yes_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "Yes", command = yes)
yes_btn.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
maybe_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "Maybe", command = yes)
maybe_btn.grid(row=5, column=2, columnspan=1, padx=5, pady=5)
no_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "No",command = no)
no_btn.grid(row=5, column=5, columnspan=1, padx=5, pady=5)
root.mainloop()

