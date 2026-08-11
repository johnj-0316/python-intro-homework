numbers = [42, 17, 83, 5, 61, 29, 74, 8, 55, 93, 31, 66, 14, 47, 78, 3, 59, 22, 86, 40]

user_input = input(
"""=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5): """)

while user_input:
    if not user_input.isdigit():
        user_input = input("Please enter a number from 1 to 5: ")
        continue
        
    user_int = int(user_input)
    
    if user_int == 1:
        minimum = float('inf')
        
        for num in numbers:
            if num < minimum:
                minimum = num
        
        print(f"\nMinimum: {minimum}\n")
        
    elif user_int == 2:
        maximum = float('-inf')
                
        for num in numbers:
            if num > maximum:
                maximum = num
        
        print(f"\nMaximum: {maximum}\n")
        
    elif user_int == 3:
        user_number = input("Enter a number: ")
        
        while not user_number.isdigit():
            print("Please try again.")
            user_number = input("Enter a number: ")
        
        for i in range(len(numbers)):
            if int(user_number) == numbers[i]:
                print(f"\nIndex: {i}\n")
                break
            elif i == len(numbers) - 1:
                print("\nnot found\n")
                
    elif user_int == 4:
        pass
                    
            
        print(f"\nSorted list: {numbers}\n")
        
    elif user_int == 5:
        print("\nThank you for using Number Cruncher. Goodbye!\n")
        break
    
    user_input = input(
    """=== Number Cruncher ===
    1. Find minimum
    2. Find maximum
    3. Search for a number
    4. Sort the list
    5. Quit
    Choose an option (1-5): """)
    
def find_min(numbers: list[int]):
    minimum = float('inf')
            
    for num in numbers:
        if num < minimum:
            minimum = num
            
    return minimum

def find_max(numbers: list[int]):
    maximum = float('-inf')
                    
    for num in numbers:
        if num > maximum:
            maximum = num
            
    return maximum

def search(numbers: list[int], target: int):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return i
        
    return -1

def bubble_sort(numbers: list[int]):
    numbers_copy = numbers.copy()
    swapped = True
    
    while swapped:
        swapped = False
        
        for i in range(1, len(numbers_copy)):
            if numbers_copy[i - 1] > numbers_copy[i]:
                temp = numbers_copy[i]
                numbers_copy[i] = numbers_copy[i - 1]
                numbers_copy[i - 1] = temp
                swapped = True
                
    return numbers_copy


def show_menu():
    user_input = input(
"""=== Number Cruncher ===
1. Find minimum
2. Find maximum
3. Search for a number
4. Sort the list
5. Quit
Choose an option (1-5): """)

    return user_input

def main():
    while (user_input := show_menu()) != "5":
        if not user_input.isdigit():
            print("Please try again.")
            continue
        
        if user_input == "1":
            print(f"\nMinimum: {find_min(numbers)}\n")
            
        elif user_input == "2":
            print(f"\nMaximum: {find_max(numbers)}\n")
            
        elif user_input == "3":
            user_number = input("Enter a number: ")
                    
            while not user_number.isdigit():
                print("Please try again.")
                user_number = input("Enter a number: ")
                
            num_index = search(numbers, int(user_number))
            
            if num_index >= 0:
                print(f"\nFound at index: {num_index}\n")
                
            else:
                print(f"Not found")
                
        elif user_number == "4":
            print()