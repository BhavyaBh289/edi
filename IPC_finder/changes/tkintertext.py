def form():
    import tkinter
    from tkinter import scrolledtext
    import fir
    root = tkinter.Tk()

    root.geometry("1920x1080")
    root.title("IPC Suggester")
    questions = tkinter.Label(root, font=("arial Bold", 30), text="IPC Suggester ")
    questions.place(x=850.0, y=30.0)
    question = tkinter.Label(root, font=("arial Bold", 15), text="Enter your statement")
    question.place(x=880.0, y=100.0)
    storylabel = scrolledtext.ScrolledText(root, wrap=tkinter.WORD,width=120, height=18,font=("arial Bold", 20))
    storylabel.place(x=50.0, y=150.0)
    # district= tkinter.Entry(root, width=1000,font=("arial Bold", 20), textvariable=story_var)
    # storyt= tkinter.StringVar()
    # storylabel.place(x=550.0, y=450.0)
    def exitt():
        global story
        story = storylabel.get("1.0","end-1c")
        root.destroy()
    button = tkinter.Button(root,command = exitt, text="Submit",font=("arial Bold", 13))
    button.place(x=930.0, y=900.0)
    root.mainloop()
    return story
