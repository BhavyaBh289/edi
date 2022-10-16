import tkinter
questionlist=[["Was there a serious death threat or grievous hurt threat?", " was the accused falling under the definition of theft , robbery, mischief, or criminal trespass?", " was there an immediate need for personal defence."], ["Was the accused of sane mind?","Did the accused intentionally commit the crime?","was there an immediate need for personal defence"]]
accepted_questions = []
x=0
y=0
def yes():

    global x,y,accepted_questions
    print ("y",x,y,len(questionlist[x]),len(questionlist))
    if y <len(questionlist[x])-1:
        y+=1
    elif y == len(questionlist[x])-1:
        y = 0
        accepted_questions.append(x)
        if x == len(questionlist)-1:
            print(accepted_questions)
            root.destroy()
            return
        x+=1
    questions.configure(text =questionlist[x][y])
def no():
    global x,y,accepted_questions
    print ("n",x,y,len(questionlist[x]),len(questionlist))
    y = 0
    if x == len(questionlist)-1:
        print(accepted_questions)
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
