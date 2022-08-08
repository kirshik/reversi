from email.mime import image
import tkinter as tk
from tkinter import messagebox
import re

from model.board import Board
from model.game import Game
from controller.game_controller import GameController
from rules.rules import ChangedRules
from player_types.human import Human
from player_types.simple_ai import SimpleAI
from player_types.advanced_ai import AdvancedAI

GEOMETRY = "1080x600"


class Reversi(tk.Tk):
    player_type = ""
    rules = ""
    board_size = 0

    def __init__(self):
        tk.Tk.__init__(self)
        self._frame = None
        self.title("Reversi / Othello")
        self.switch_frame(MenuPlayerType)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self)
        if self._frame is not None:
            self._frame.destroy()
        self._frame = new_frame
        self._frame.pack()

    def handle_options(self, button: "MenuButton"):
        if button.type == "human":
            self.player_type = 1
        elif button.type == "simple_ai":
            self.player_type = 2
        elif button.type == "advanced_ai":
            self.player_type = 3
        elif button.type == "open_rules":
            self.player_type = "open_rules"
        elif button.type == "standart_rules":
            self.player_type = "standart_rules"
        # elif re.search("\d+", button.type):
        #     self.board_size = int(button.type)


class MenuPlayerType(tk.Frame):

    def __init__(self, master):
        tk.Frame.__init__(self, master)
        btn_human = MenuButton(master=self, type="human", text="1 vs 1")
        btn_simple_ai = MenuButton(
            master=self, type="simple_ai", text="play with easy bot")
        btn_advanced_ai = MenuButton(
            master=self, text="play with hard bot", type="advanced_ai")

        btn_human.config(command=lambda button=btn_human: [master.switch_frame(
            ChooseRules), master.handle_options(button)])
        btn_simple_ai.config(command=lambda button=btn_simple_ai: [master.switch_frame(
            ChooseRules), master.handle_options(button)])
        btn_advanced_ai.config(command=lambda button=btn_advanced_ai: [master.switch_frame(
            ChooseRules), master.handle_options(button)])

        btn_human.pack()
        btn_simple_ai.pack()
        btn_advanced_ai.pack()


class ChooseRules(tk.Frame):
    def __init__(self, master):

        tk.Frame.__init__(self, master)
        btn_open_rules = MenuButton(
            master=self, text="playing with \"open\" rooles\n where you can put disks anywere", type="open_rules")
        btn_standart_rules = MenuButton(
            master=self, text="Play standart rooles", type="standart_rules")

        btn_open_rules.config(command=lambda button=btn_open_rules: [master.switch_frame(
            ChooseBoard), master.handle_options(button)])
        btn_standart_rules.config(command=lambda button=btn_standart_rules: [master.switch_frame(
            ChooseBoard), master.handle_options(button)])

        btn_go_back = MenuButton(master=self, type="None", text="go back", command=lambda: master.switch_frame(
            MenuPlayerType))

        btn_open_rules.pack()
        btn_standart_rules.pack()
        btn_go_back.pack()


class ChooseBoard(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        tk.Label(self, text="Enter board size", justify="center")

        def createBoard():
            return game(master, master.board_size, master.rules, master.player_type)
            pass

        def display():
            if not re.search("\d+", board_size.get()):
                messagebox.showinfo("Error",
                                    f"Invalid board size: {board_size.get()}")
            else:
                master.board_size = int(board_size.get())
                btn_next.config(
                    command=createBoard)

        board_size = tk.Entry(self, width=10, font=(
            "Verdana", 35, "bold"), justify="center")
        btn_next = MenuButton(
            master=self, text="Choose board size", type=board_size.get())

        btn_next.config(command=display)

        btn_go_back = MenuButton(master=self, type="None", text="go back", command=lambda: master.switch_frame(
            ChooseRules))
        board_size.pack()
        btn_next.pack()
        btn_go_back.pack()


def game(app, board_size, rule, player_type):
    board_window = tk.Toplevel(app)
    board_window.geometry(GEOMETRY)
    label = tk.Label(board_window, text="Reversi Game").grid(column=0, row=0)

    board = Board(board_size)
    game = Game(board)
    if player_type == 1:
        player_type = Human()
    elif player_type == 2:
        player_type = SimpleAI(board, game)
    elif player_type == 3:
        player_type = AdvancedAI(board, game)
    if rule == "open_rules":
        game_controler = GameController("graphic", game, player_type)
        game_controler.run_game()
    else:
        game_controler = ChangedRules(board)
    buttons = []
    for i in range(board_size):
        row = []
        for j in range(board_size):
            btn = tk.Button(
                app, text=board.get_cell(i, j))

            row.append(btn)
        buttons.append(row)
    for i in range(board_size):
        for j in range(board_size):
            btn = buttons[i][j]
            btn.grid(row=i, column=j)


class CellButton(tk.Button):
    def __init__(self, text, row, col, command=None, master=None, *args, ** kwargs):
        self.row = row
        self.col = col
        self.text = text
        if col % 2 == 0:
            self.background = "#BAB7B7"
        else:
            self.background = "#FFFFFF"
        self.command = command
        super(CellButton, self).__init__(master)
        self["text"] = self.text
        self['command'] = self.command
        self["background"] = self.background
        # self["padx"] = 200
        # self["width"] = 150
        # self["pady"] = 50
        # self["font"] = ("Verdana", 35, "bold")
        self["justify"] = "center"


class MenuButton(tk.Button):

    def __init__(self, text, type, command=None, master=None, *args, ** kwargs):
        self.type = type
        self.text = text
        self.background = "#B6ECEA"
        self.command = command
        super(MenuButton, self).__init__(master)
        self["text"] = self.text
        self['command'] = self.command
        self["background"] = self.background
        self["padx"] = 200
        self["width"] = 150
        self["pady"] = 50
        self["font"] = ("Verdana", 35, "bold")
        self["justify"] = "center"
        self["relief"] = "groove"


if __name__ == "__main__":
    app = Reversi()
    app.geometry(GEOMETRY)
    app.mainloop
