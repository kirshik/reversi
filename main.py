from view.menu_view import Menu

menu = Menu()
game_start = input(
    "Please print \"start\" to start the game\n and \"close\" to finish the programm:  ")
while game_start != "close":
    menu.menu()
    game_start = input(
        "Please print \"start\" to start the game\n and \"close\" to finish the programm:  ")
