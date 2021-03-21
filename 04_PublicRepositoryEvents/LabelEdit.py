import tkinter as tk

class Application(tk.Frame):
	def __init__(self, master=None):
		super().__init__(master)
		self.master.rowconfigure(0, weight=1)
		self.master.columnconfigure(0, weight=1)
		self.grid(sticky='NEWS')
		self.createWidgets()

	def createWidgets(self):
		self.textWindow = TextWindow(self)
		self.quitButton = tk.Button(self, text='Exit', command=self.quit)

		self.textWindow.grid(sticky='EW')
		self.quitButton.grid(sticky='S')

		self.columnconfigure(0, weight=1)
		self.rowconfigure(1, weight=1)


class TextWindow(tk.Label):
	def __init__(self, master=None):
		self.text = tk.StringVar()
		super().__init__(master, textvariable=self.text, font='Fixedsys', takefocus=1, highlightthickness=1, anchor='w')
		self.bind('<Button-1>', self.klik)
		self.bind('<KeyPress>', self.button)

		self.pos = 0
		self.textCursor = tk.Frame(self, background='red', width=1)
		self.textCursor.place(x=self.pos, y=0, height=20)

	def klik(self, event):
		self.focus()
		self.pos = event.x // 10 * 10
		if self.pos > len(self.text.get()) * 10:
			self.pos = len(self.text.get()) * 10
		self.textCursor.place(x=self.pos)

	def button(self, event):
		if event.keysym == 'Home':
			self.pos = 0
			self.textCursor.place(x=self.pos)
		elif event.keysym == 'End':
			self.pos = len(self.text.get()) * 10
			self.textCursor.place(x=self.pos)
		elif event.keysym == 'Right':
			self.pos += 10
			if self.pos > len(self.text.get()) * 10:
				self.pos = len(self.text.get()) * 10
			self.textCursor.place(x=self.pos)
		elif event.keysym == 'Left':
			self.pos -= 10
			if self.pos < 0:
				self.pos = 0
			self.textCursor.place(x=self.pos)
		elif event.keysym == 'BackSpace':
			t = self.text.get()
			i = self.pos // 10
			if i:
				t = t[ : i - 1] + t[i:]
				self.text.set(t)
				self.pos -= 10
				self.textCursor.place(x=self.pos)
		elif event.keysym == 'Delete':
			t = self.text.get()
			i = self.pos // 10
			if i != len(self.text.get()):
				t = t[ : i] + t[i + 1:]
				self.text.set(t)
				self.textCursor.place(x=self.pos)
		elif event.char.isprintable():
			t = self.text.get()
			i = self.pos // 10
			t = t[:i] + event.char + t[i:]
			self.pos += 10
			self.text.set(t)
			self.textCursor.place(x=self.pos)







app = Application()
app.mainloop()