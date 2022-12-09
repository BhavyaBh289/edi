import ctkintere
import tkintertext
import printobj
import fir
test = ctkintere.form()
# print(test.District)
story = tkintertext.form()
# print (story)
test.story = story
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '1'
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
sample = story.lower()
def keywordextract():
    global n , sample
    extractor = pke.unsupervised.TopicRank()
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
    # print(n, i)
def keyword_changing():
    #keyword adding and removing
    global n , sample
    t = []
    # print("before",n)
    verb =["can","got", "gave","take", "will","according","given","said"]
    synonyms=[["beat","hurt","abuse","assault"],["kill""murder"],["sexual","rape"],["abetment","influence"]]
    nouns=["Authority","officer", "hospital", "weapon", "girl", "coin","money","drug","dowry"]
    for i in n :
        if i in verb :
            pass
        else:
            t.append(i)
    n = t
    # for i in synonyms:
    #     if
    for i in nouns:
        if i in sample:
            n.append(i)
    # print("after",n)

def bmitoquest():
    global questionlist,ips,df,n
    ld = df["3"]
    languagedata = [doc.split(" ") for doc in ld]
    bm25 = BM25Okapi(languagedata)
    doc_scores = bm25.get_scores(n)
    questionlist = []
    ips = []
    tp = []
    t=-2
    tempstr="test"
    for i in doc_scores:
        t+=1
        if i > 0.1:
            ips.append(t)
            tp.append(df["1"][t])
            temp=[df["4"][t],df["5"][t],df["6"][t]]
            temp2=[]
            for temp3 in temp:
                if type(temp3)==type(tempstr):
                    temp2.append(temp3)
            questionlist.append(temp2)
    # print(questionlist,tp)

keywordextract()
keyword_changing()
bmitoquest()



def exitt():
    global accepted_questions,ips,df,n,test
    finalipcs = []
    for i in accepted_questions :
            finalipcs.append(df["1"][ips[i]])
    t = [["120","120B"],["159","160"],["310","311"],['339','341'],['340','342'],['375','376'],['378','379'],['383','384'],['390','392'],['391','395'],['415','417'],['425','426'],['499','500']]
    for i in finalipcs:
        for b in t:
            if i in b :
                finalipcs.append(b[1])
    with open("myfile.txt", 'a') as file1:
        file1.write(str(n))
        for i in finalipcs :
            print(i)
            file1.write(str(i+" "))
        file1.write("\n")
    test.ipc = finalipcs
    printobj.write(test)

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
    #print ("n",x,y,len(questionlist[x]),len(questionlist))
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
maybe_btn.grid(row=7, column=0, columnspan=1, padx=5, pady=5)
no_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "No",command = no)
no_btn.grid(row=9, column=0, columnspan=1, padx=5, pady=5)
root.mainloop()


