day_input = input("What day is it? ")
time_input = input("What time of day? ") # morning, afternoon, evening
day = day_input.lower()
time = time_input.lower()
result = "Suggestion: "

if day == "sunday":
    if time == "morning":
        result += "Sleep in — it's a day of rest!"
    elif time == "afternoon":
        result += "Great time to walk outside or crochet something new."
    elif time == "evening":
        result += "Make sure you're prepared for the week... or go watch a movie."
    else:
        result = "Sorry, I only recognize \"morning\", \"afternoon\", or \"evening\"..."

elif day == "monday":
    if time == "morning":
        result += "Go to the gym to start the week off strong!"
    elif time == "afternoon":
        result += "Busy day — practice some LeetCode or work on any current projects."
    elif time == "evening":
        result += "Treat yourself... you made it through arguably the hardest day of the week!"
    else:
        result = "Sorry, I only recognize \"morning\", \"afternoon\", or \"evening\"..."

elif day == "tuesday":
    if time == "morning":
        result += "Look outside — play some music that fits the weather."
    elif time == "afternoon":
        result += "See if any of your friends are free for plans. If not, play some video games!"
    elif time == "evening":
        result += "Evening Python group session — great time to focus!"
    else:
        result = "Sorry, I only recognize \"morning\", \"afternoon\", or \"evening\"..."
        
elif day == "wednesday":
    if time == "morning":
        result += "Halfway there! Make your \"guilty-pleasure\" breakfast~"
    elif time == "afternoon":
        result += "Go for a run if possible! Surprisingly, it helps with your mental health."
    elif time == "evening":
        result += "Call someone you haven't talked to in a while! Talk about anything you want."
    else:
        result = "Sorry, I only recognize \"morning\", \"afternoon\", or \"evening\"..."

else:
    result = "Sorry, I don't recognize that day. Try: Monday, Tuesday, Wednesday..."

print(result)