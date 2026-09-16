Project Title: PokéWeb

A mini project displaying a small menu.

API used: PokeAPI (https://pokeapi.co/) to fetch pokemon and types data.
The program displays simple UI in the terminal which handles searching and filtering.

Description: Inputs are done via input() in the terminal.
A menu will appear after the program runs. Enter a valid number input according to the action you would like to perform. 
Afterwards, enter a valid input. Pokemon data will be displayed via table, while pokemon based on type will be displayed via a paginated list of 10.

On inputs that require a yes, you may enter "yes", "ye", or "y", disregarding case, to repeat the action. Otherwise, all other inputs are treated as a "no".
Invalid inputs will immediately stop the action and display an appropriate error.

How to install and run:
Ensure all packages from requirements.txt are installed properly, including requests.
No API keys needed!
To run, make sure you have a valid Python interpreter. Then, either set up a .venv environment and run "python main.py", or simply run "python3 main.py". Replace "3" with the top version of your Python interpreter. 