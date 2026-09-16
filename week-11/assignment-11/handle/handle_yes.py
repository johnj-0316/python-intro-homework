def handle_yes(action: str):
    yes_answers = {"y", "ye", "yes"}
    return input(f"Would you like to continue with {action}? ").lower() in yes_answers