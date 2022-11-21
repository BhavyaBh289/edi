import pandas as pd
from rank_bm25 import BM25Okapi
import tkinter
df = pd.read_csv("IPC_whole - IPC_whole.csv")
def bmitoquest():
    global questionlist,ips,df
    inp = ['Shankra-Kh', 'abusing', 'beat', 'beating', 'letting', 'eat', 'tried', 'survive', 'paying', 'increased', 'told', 'told', 'buy', 'came', 'convince', 'insulted', 'sent', 'leaving', 'given', 'replaced', 'come', 'kill', 'remarry', 'remarried', 'want', 'return', 'demanding', 'know', 'remarrieddid','father-deceased', 'punish', 'secure', 'delayed', 'hoping']
    ld = df["3"]
    languagedata = [doc.split(" ") for doc in ld]
    bm25 = BM25Okapi(languagedata)
    doc_scores = bm25.get_scores(inp)
    questionlist = []
    ips = []
    n=-2
    for i in doc_scores:
        n+=1
        if i > 0.1:
            ips.append(n)
            questionlist.append([df["4"][n],df["5"][n],df["6"][n]])
    # print(questionlist,ips)
ips=[]
questionlist=[]
accepted_questions = []
x=0
y=0
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
    global x,y,accepted_questions
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
# questions.configure(text = "question1")
yes_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "Yes", command = yes)
yes_btn.grid(row=5, column=0, columnspan=1, padx=5, pady=5)
maybe_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "Maybe", command = yes)
maybe_btn.grid(row=5, column=2, columnspan=1, padx=5, pady=5)
no_btn = tkinter.Button(root,font=("Times New Roman", 25),text = "No",command = no)
no_btn.grid(row=5, column=5, columnspan=1, padx=5, pady=5)
root.mainloop()
