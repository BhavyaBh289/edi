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
sample = """This time Re.Po.St. G.R.No. of Thane. 00/2018 c. 392,34 Document of crime in Hon. Superintendent of Police Received from Aurangabad, Ma pso So. We are filing a case as per his orders. () Name of Plaintiff :- Vivek Gupteshwar Singh Age 31 years Res. Village Renukuot Yugandh Colony Duddhi District, Sonbhadra U.P. Md. 8853053016) Name and Address of Accused:- Tea Seller Isam Age No. 18 to 22 years Ranga black slim and his three companions age 23 to 24 years second 25 years third age 12 to 13 years () Up Ghad Seat Train.No. Up 11062 Pawan X Coach 5/7 Berth 76 from Re.St. After the train departs from Jalgaon () Up Ghad Ta. Time :- Dt. 19/11/2018 at 20.00 hrs. Around () up da., h. time d. 04/12/2018 As Margin ( ) Stolen Goods Cash Rs. 2500/-Rs. (2000x1.500x1) a total of Rs.2500. ( ) got the goods :- Nirank () facts such that on the said date the plaintiff was traveling from Varanasi to Thane by the said coach and Barkh of the said train and during the journey the said Rai.St. After leaving Jalgaon, Isma, who was selling tea of ​​the above description, had a verbal altercation with him for the reason of paying extra money for the tea, and got together with his three accomplices of the above description, beat them on the face with kicks and abused them, and among them Isma, who was a French cut grandmother of the above description, took the cash of the above description from their hands. According to the complaint given by them, they left by stealing the rupees. According to 392,34 IPC, uniform report was filed by Ms. JMFC. The Railway Court has ordered Bhusawal to be sent for further investigation of the crime Hon.PI Shri. Gadhri So. doing this."""
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
    nouns=["Authority","officer", "hospital", "weapon", "girl", "coin","money","drug"]
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
maybe_btn.grid(row=5, column=2, columnspan=1, padx=5, pady=5)
no_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "No",command = no)
no_btn.grid(row=5, column=5, columnspan=1, padx=5, pady=5)
# root.mainloop()
