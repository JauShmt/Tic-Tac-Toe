import tkinter as tk

class MainWindow:

    def __init__(self, game):

        self.main_window=tk.Tk()
        self.main_window.title('Tic Tac Toe')
        self.reset= tk.Menu(self.main_window)
        self.reset.add_command(label='Reset Game', command=self.reset_btns)
        self.reset_btns()
        self.clicked = False
        self.count = 0
        self.game = game


    def reset_btns(self):
        self.b1 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b1))
        self.b2 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b2))
        self.b3 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b3))
        self.b4 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b4))
        self.b5 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b5))
        self.b6 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b6))
        self.b7 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b7))
        self.b8 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b8))
        self.b9 = tk.Button(self.main_window, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace", command=lambda: self.click_btns(self.b9))

        self.b1.grid(row=0, column=0)
        self.b2.grid(row=0, column=1)
        self.b3.grid(row=0, column=2)

        self.b4.grid(row=1, column=0)
        self.b5.grid(row=1, column=1)
        self.b6.grid(row=1, column=2)

        self.b7.grid(row=2, column=0)
        self.b8.grid(row=2, column=1)
        self.b9.grid(row=2, column=2)

        self.count = 0


    def click_btns(self,b):
        if b["text"] == " " and self.clicked == True:
            b["text"] = "X"
            self.clicked = False
            self.count += 1
            self.game.checkifwon(self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self, self.count)
        elif b["text"] == " " and self.clicked == False:
            b["text"] = "O"
            self.clicked = True
            self.count += 1
            self.game.checkifwon(self.b1, self.b2, self.b3, self.b4, self.b5, self.b6, self.b7, self.b8, self.b9, self, self.count)

    def disable_all_buttons(self):
        self.b1.config(state=tk.DISABLED)
        self.b2.config(state=tk.DISABLED)
        self.b3.config(state=tk.DISABLED)
        self.b4.config(state=tk.DISABLED)
        self.b5.config(state=tk.DISABLED)
        self.b6.config(state=tk.DISABLED)
        self.b7.config(state=tk.DISABLED)
        self.b8.config(state=tk.DISABLED)
        self.b9.config(state=tk.DISABLED)


    def run(self):
        self.main_window.mainloop()

    def get_count(self):
        return self.count



