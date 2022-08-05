from tkinter import *

root = Tk()
root.title("Reversi / Othello")
root.geometry("1080x720")


class MenuButton(Button):

    def __init__(self, text, **kwargs):
        self.text = text
        self.background = "#555"
        super().__init__()
        self["text"] = self.text
        self["background"] = self.background
        self["padx"] = 200
        self["width"] = 150
        self["pady"] = 50
        self["font"] = ("Verdana", 35, "bold")


button_play_human = MenuButton(text="      1 vs 1      ")
button_play_simple_ai = MenuButton(text="play with easy bot")
button_play_advanced_ai = MenuButton(text="play with hard bot")
button_play_human.pack()
button_play_simple_ai.pack()
button_play_advanced_ai.pack()

root.mainloop()
