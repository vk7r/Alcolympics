# Welcome to Alcolympics! 🍻🏅

To proceed, you **MUST** follow the sacred rules of the game:

1. **DO NOT TOUCH main.py**

2. 🎉 **Have Fun**

3. 🔁 **Follow Rule 1 & 2**

## Got an idea of a game? Contribute! (shurda)

`main.py` contains the game’s main loop, a terminal-based menu that serves as the hub and dynamically adds all games placed in the `games/` folder.

You can build your game with any GUI or language you like, but it **MUST** be wrapped in a Python file so it can be integrated with the main loop.

Create a new folder inside `games/` with your game's full name — this name will be displayed in the main menu.  
Your main file **MUST** be named **`start.py`** and **MUST** include a **`start_game()`** function, which will be called by the main loop to run your game.

You can use the `GameSession` class provided by `main.py` to access all relevant game session data for your game.

Don’t forget to add any new dependencies your game needs into requirements.txt.
