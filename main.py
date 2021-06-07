import requests
from jokeapi import Jokes
from tkinter import *
from tkinter import messagebox
window = Tk()
textmsg = Label(window)
boxmessage = StringVar()
message = ''
flags = []
window.geometry("400x268")
window.resizable(False, True)
window.title('Jokes')
def getjoke():
	j = Jokes()
	currentjoke = j.get_joke()
	joke = currentjoke
	flag = currentjoke['flags']
	if flag['nsfw']:
		flags.append('nsfw')
	if flag['religious']:
		flags.append('religious')
	if flag['political']:
		flags.append('political')
	if flag['racist']:
		flags.append('racist')
	if flag['sexist']:
		flags.append('sexist')
	if flag['explicit']:
		flags.append('explicit')
	if flags:
		strf = str(flags)
		temp = strf.replace(']', '')
		temp2 = temp.replace('[', '')
		strf = temp2.replace("'", '')
		ucontinue = messagebox.askyesno(title='continue?', message=f'This Joke may contain {strf} content. Are you sure you want to proceed?')
		flags.clear()
		if not ucontinue:
			boxmessage.set('[Joke removed]')
			return
	if joke["type"] == "single":
		message = joke["joke"]
		boxmessage.set(message)
	else:
		message = f'This joke requires a setup and delivery:\n setup: {joke["setup"]}\ndelivery: {joke["delivery"]}'
		boxmessage.set(message)
textmsg.configure(textvariable=boxmessage,wrap=400)
textmsg.pack(side='bottom')
btn_joke = Button(window, command=getjoke, text='Joke')
btn_joke.pack(side='top')
window.mainloop()