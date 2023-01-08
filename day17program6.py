from tkinter import*
master=Tk()
demo_text="This is sample demo of message widget"
msg=Message(master, text=demo_text)
msg.config(bg='blue',font=('times',24,'bold'))
msg.pack()
