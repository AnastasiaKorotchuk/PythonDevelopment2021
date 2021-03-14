import tkinter as tk
import random
from tkinter import messagebox as mb

n = 16


class Application(tk.Frame):
    playButtons = [0] * n
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.grid(sticky='NEWS')
        self.createWidgets()

    def show_win(self):
        msg = "YOU WIN!"
        mb.showinfo("Information", msg)
        self.makePlayButtons()

    def move(self, num): 
        def move2(self=self, num=num):
            index = self.numbers.index(num)
            r = index // 4
            c = index % 4
            if r - 1 >= 0 and self.numbers[4 * (r - 1) + c] == 0:
                self.numbers[4 * (r - 1) + c], self.numbers[index] = self.numbers[index], self.numbers[4 * (r - 1) + c]
                self.playButtons[index].grid(row=r - 1 + 1, column=c)
                self.playButtons[4 * (r - 1) + c], self.playButtons[index] = self.playButtons[index], self.playButtons[4 * (r - 1) + c]

            elif r + 1 <= 3 and self.numbers[4 * (r + 1) + c] == 0:
                self.numbers[4 * (r + 1) + c], self.numbers[index] = self.numbers[index], self.numbers[4 * (r + 1) + c]
                self.playButtons[index].grid(row=r + 1 + 1, column=c)
                self.playButtons[4 * (r + 1) + c], self.playButtons[index] = self.playButtons[index], self.playButtons[4 * (r + 1) + c]
            elif c + 1 <= 3 and self.numbers[4 * r + c + 1] == 0:
                self.numbers[4 * r + c + 1], self.numbers[index] = self.numbers[index], self.numbers[4 * r + c + 1]
                self.playButtons[index].grid(row=r + 1, column=c + 1)
                self.playButtons[4 * r + c + 1], self.playButtons[index] = self.playButtons[index], self.playButtons[4 * r + c + 1]
            elif c - 1 >= 0 and self.numbers[4 * r + c - 1] == 0:
                self.numbers[4 * r + c - 1], self.numbers[index] = self.numbers[index], self.numbers[4 * r + c - 1]
                self.playButtons[index].grid(row=r + 1, column=c - 1)
                self.playButtons[4 * r + c - 1], self.playButtons[index] = self.playButtons[index], self.playButtons[4 * r + c - 1]
            if self.numbers == [i % 16 for i in range(1, 17)]:
                self.show_win()
        return move2    

    def makePlayButtons(self):
        for but in self.playButtons:
            if but != 0:
                but.destroy()

        self.numbers = [i for i in range(n)]
        random.shuffle(self.numbers)

        self.playButtons = [0] * n
        for i in range(n):
            if self.numbers[i] == 0:
                continue
            self.playButtons[i] = tk.Button(self, text=str(self.numbers[i]), command=self.move(self.numbers[i]))
            self.playButtons[i].grid(row=i // 4 + 1, column=i % 4, sticky='SENW')



    def createWidgets(self):
        

        self.quitButton = tk.Button(self, text='Exit', command=self.quit)
        self.newButton = tk.Button(self, text='New', command=self.makePlayButtons)

        self.makePlayButtons()

        self.quitButton.grid(row=0, column=0)
        self.newButton.grid(row=0, column=2)

        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight = 1)

        for r in range(1, 5):
            self.rowconfigure(r, weight = 1)
        for c in range(4):
           self.columnconfigure(c, weight = 1)
        #self.show_win()

app = Application()
app.master.title('15 puzzle')
app.mainloop()