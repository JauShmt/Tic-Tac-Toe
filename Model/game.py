from tkinter import messagebox
from GUI.MainWindow import MainWindow

class Game:


    def checkifwon(self, b1, b2, b3, b4, b5, b6, b7, b8, b9, main_window, count):
        self.winner = False

        if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()
        elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

        elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  X Wins!!")
            main_window.disable_all_buttons()

            #### CHECK FOR O's Win
        elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
            b1.config(bg="red")
            b2.config(bg="red")
            b3.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
            b4.config(bg="red")
            b5.config(bg="red")
            b6.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
            b7.config(bg="red")
            b8.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
            b1.config(bg="red")
            b4.config(bg="red")
            b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
            b2.config(bg="red")
            b5.config(bg="red")
            b8.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
            b3.config(bg="red")
            b6.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
            b1.config(bg="red")
            b5.config(bg="red")
            b9.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

        elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
            b3.config(bg="red")
            b5.config(bg="red")
            b7.config(bg="red")
            self.winner = True
            messagebox.showinfo("Tic Tac Toe", "CONGRATULATIONS!  O Wins!!")
            main_window.disable_all_buttons()

            # Check if tie
        if count == 9 and self.winner == False:
            messagebox.showinfo("Tic Tac Toe", "It's A Tie!\n No One Wins!")
            main_window.disable_all_buttons()




