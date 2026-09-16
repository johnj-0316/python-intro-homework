from get.get_by_type import get_by_type
from chart.chart_data import chart_data
from chart.chart_display import chart_display
from handle.handle_yes import handle_yes

def handle_chart(type: str):
    try:
        while True:
            if not isinstance(type, str):
                    print("The input type is not a string!")
                    return
                
            if not type:
                print("Please enter a type into the field below.")
                return
            
            type = type.lower()
            res = get_by_type(type)
            
            if not res:
                print("There was a problem with your input. Please try again.")
                return
            
            print("Displaying frequency chart...")
            pokemon = chart_data(res)
            chart_display(f"How frequent does the {type.capitalize()} type appear as the 1st and 2nd slot for all pokemon?", pokemon["categories"], pokemon["quantities"])
            
            if not handle_yes("displaying slot frequencies (Y/n)"):
                break
            
            type = input("Enter a valid pokemon type: ").lower()
    except Exception as e:
        print(f"Something went wrong with searching for the pokemon. {e}")