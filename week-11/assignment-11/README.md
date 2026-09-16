Project Title: PokéWeb

A mini project displaying a small menu.

API used: PokeAPI (https://pokeapi.co/) to fetch pokemon and types data.
The program displays simple UI in the terminal which handles searching and filtering.

Description: Inputs are done via input() in the terminal.
A menu will appear after the program runs. Enter a valid number input according to the action you would like to perform. 
Afterwards, enter a valid input. Pokemon data will be displayed via table, while pokemon based on type will be displayed via a paginated list of 10.

On inputs that require a yes, you may enter "yes", "ye", or "y", disregarding case, to repeat the action. Otherwise, all other inputs are treated as a "no".
Invalid inputs will immediately stop the action and display an appropriate error.

## Visualization
Choice A
The extension uses matplotlib to create a small bar graph, detailing how frequent a chosen type is in certain slots. For context, all pokemon have types, but some have 2 types. For those with 2, while the order of the type does not matter too much, it is interesting to see how prominent certain types are in certain slots (is water more common as the first or second type)? Using the API, built in Counter from collections module, and a matplotlib, the extension counts the frequencies and compares the two visually.

Question: "How frequent does the {type chosen, i.e. electric} type appear as the 1st and 2nd slot for all pokemon?"

Visualization starts with the x axis labeled as slot 1 or slot 2, the y axis showing the frequency counts, and the title reflecting the chosen type. The color chosen for the bars is blue, and each bar shows the actual frequency above it.

The repo will show a demo of the type "electric".

How to install and run:
Ensure all packages from requirements.txt are installed properly, including requests.
No API keys needed!
To run, make sure you have a valid Python interpreter. Then, either set up a .venv environment and run "python main.py", or simply run "python3 main.py". Replace "3" with the top version of your Python interpreter. 