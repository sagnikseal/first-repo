from tkinter import *
import tkinter as tk
from gtts import gTTS
from playsound import playsound
from functools import *
import os
import winsound
c=[1]
window = Tk()
window.geometry('530x530')
window.title('Text To Speech')
text = Text(window, height = 25, width = 50)
scroll = Scrollbar(window, command = text.yview)
text.configure(yscrollcommand = scroll.set)
text.tag_configure('bold italics', font=('Verdana',12,'bold','italic'))
text.tag_configure('big',font=('Verdana',24,'bold'))
text.tag_configure('color',foreground='blue',font=('Tempus Sans ITC',14))
text.tag_configure('groove',relief=GROOVE,borderwidth=2)
text.tag_bind('bite','<1>',lambda e, text=text: text.insert(END,"Text"))
text.pack(side=LEFT)
scroll.pack(side=RIGHT,fill=Y)
def convert(text):
	t=text.get('1.0',END)
	try:
                os.remove('speech.mp3')
        except:
                pass
	tts=gTTS(t)
	f='speech'+'.mp3'
	tts.save(f)
	playsound(f)
	print("hi")
	os.remove(f)
	c[0]+=1
	print("1")
btn = Button(window, text='Speak', command = partial(convert,text))
btn.pack(side = RIGHT)
def about():
	about_window = tk.Tk()
	about_window.title("About")
	about_window.resizable(0, 0)
	about_window.geometry("600x600")
	about_label = tk.Label(about_window, text="About", font=("times new roman", 16, "bold"))
	about_label.place(x=10, y=10)
	about_file = open("about.txt", "r")
	about_contents_label = tk.Label(about_window, text=about_file.read(), font=("times new roman", 10, "normal"))
	about_contents_label.place(x=10, y=80)
	about_file.close()
fr= Frame(window)
fr.pack(side=TOP, expand = FALSE,fill = X)
abt=Button(fr,text='About',command = partial(about),padx=100,relief = GROOVE, justify = CENTER)
abt.pack(side=RIGHT)




