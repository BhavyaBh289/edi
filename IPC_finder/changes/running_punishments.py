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
sample = """ Sir, my humble submission to you is that I am Roshan Bibi Swami Sikh Sabarak Darji, Village:-Shankra-Kh,Po:-Shankra,Thana:-Para,Dist:- Purulia resident.As per Muslim Neon last dated 05.09.2017 Married to Sekh Sabarak Darji, son of Sekh Jugnu Darji of village Shankra-Kh under Para police station.Currently, I am the mother of a 03-year-old son, from the last one year, my husband and in-laws have been abusing me mentally and physically in various ways. They also beat my three-year-old child by not letting him eat or verbally beating him. I have tried to survive in the world despite all the tortures. After paying all the dowry during the marriage, the torture on me increased for the last nine-ten months, and I was repeatedly told by them to buy my father a Bullet car. Then my father and brother came to convince my in-laws and insulted them and sent me and my child to my father's house on 29-09-2021. While leaving, my brother-in-law and mother-in-law told me that the Hero Glamor whose registration number JH09AG 6215 was given as dowry during the marriage should be replaced by a new BULLET car, otherwise they should come back or kill their son i.e. me. Husband will remarry. Even though I want to return to in-laws house again and again, my husband or in-laws keep humiliating me and demanding a new BULLET car. is doing Now I know for sure that my husband is remarrieddid So sir my husband 1) Sikh Sabarak Darji, 2) Vasur Sikh Tabarak Darji, 3) Nand-Parbina Bibi, 4) Sikh Jaganu Darji father-deceased Nishad Darji and 5) Mother-in-law Khairuna Bibi, husband- Jaganu Darji legal action against all of them. Take appropriate measures to punish the maidservants and take necessary steps to secure the future life of me and my children. My complaint was delayed because I was hoping it would take me now that my husband had remarried."""
sample = sample.lower()
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
    print("after",n)

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
    print(questionlist,tp)

keywordextract()
keyword_changing()
bmitoquest()



def exitt():
    global accepted_questions,ips,df,n
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


