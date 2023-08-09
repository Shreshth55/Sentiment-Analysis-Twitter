from tkinter import *
from tkinter.ttk import *
from stream import project

obj = project()

tk = Tk()
tk.title("Sentimental Analyser (Twitter)")
tk.resizable(0, 0)
upper = Frame(tk)
l1 = Label(upper, text="Keyword Or HashTag:", font='Courier')
l1.grid(row=0, column=0)
searchTerm = StringVar()
searchTerm_var = Entry(upper, textvariable=searchTerm, width=30)
searchTerm_var.grid(row=0, column=1, padx=10)

l2 = Label(upper, text="Number Of Tweets To Analyse:", font='Courier')
l2.grid(row=0, column=2, padx=10)
noOfSearchTerm = IntVar()
noOfSearchTerm_var = Entry(upper, textvariable=noOfSearchTerm)
noOfSearchTerm_var.grid(row=0, column=3)

upper.grid(row=0, column=0, pady=20, sticky='nsew', padx=30)

sep = Separator(tk, orient="horizontal")
sep.grid(row=1, column=0, sticky='ew')
l3 = Label(tk, text="Optional Twitter API Entries", font='Courier')
l3.grid(row=2, column=0)

lower = Frame(tk)
l4 = Label(lower, text="Consumer Key:", font='Courier')
l4.grid(row=0, column=0)
consumer_key = StringVar()
consumer_key_var = Entry(lower, textvariable=consumer_key, width=60)
consumer_key_var.grid(row=0, column=1, pady=20)

l5 = Label(lower, text="Consumer Secret key:", font='Courier')
l5.grid(row=1, column=0)
consumer_secret_key = StringVar()
consumer_secret_key_var = Entry(lower, textvariable=consumer_secret_key, width=60)
consumer_secret_key_var.grid(row=1, column=1, pady=10)

l6 = Label(lower, text="Access Token:", font='Courier')
l6.grid(row=2, column=0)
access_token = StringVar()
access_token_var = Entry(lower, textvariable=access_token, width=60)
access_token_var.grid(row=2, column=1, pady=20)

l7 = Label(lower, text="Access Secret Token:", font='Courier')
l7.grid(row=3, column=0)
access_secret_token = StringVar()
access_secret_token_var = Entry(lower, textvariable=access_secret_token, width=60)
access_secret_token_var.grid(row=3, column=1, pady=20)

l8 = Label(lower, text="File Name To Store Tweet Info:", font='Courier')
l8.grid(row=4, column=0)
file = StringVar()
file_var = Entry(lower, textvariable=file, width=60)
file_var.grid(row=4, column=1, pady=20)


def call():
    obj.tweetFeed(searchTerm.get(), noOfSearchTerm.get(), consumer_key="CvFNEUlZP81P72ekyIXxGBdfw",
                  consumer_secret_key="wIU1HVQppKRn2IIvWIYRHMIwxPGalq9SDibNLXVqVbZS5ZF4fR",
                  access_token="1074979255535034368-qDWcYDg0Aq3rbU4s8vDAp014oIc6gz",
                  access_secret_token="eFYs7wlDjKmslNzs6TpgDHrPoK0qqrCQ0TbQNLvmfhKR5", file=file.get())
    obj.graph()


go = Button(lower, text="GO", command=call, width=30)
go.grid(row=5, pady=20, columnspan=3)
lower.grid(row=3, column=0, sticky='nsew', padx=20)

tk.mainloop()
