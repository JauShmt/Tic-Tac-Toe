from GUI.MainWindow import MainWindow
from Model.game import Game


game = Game()

# Creation of the GUI object
main_window = MainWindow(game)


# Starts the GUI
main_window.run()
