# Create a file called my_toolkit.py containing the following functions. Each function must include a docstring explaining what it does.

# calculate_average(numbers) — Takes a list of numbers, returns the average. Returns 0 if the list is empty.

def calculate_average(numbers):
    """
    Takes a list of numbers and returns their average.
    Returns 0 if the list is empty.
    """
    if not numbers:
        return 0
    
    return sum(numbers) / len(numbers)

# find_max_and_min(numbers) — Takes a list of numbers, returns a tuple (max_value, min_value). Do NOT use the built-in max() and min() — implement the logic yourself with a loop.
def find_max_and_min(numbers):
    if not numbers:
        return None
    max_value = numbers[0]
    min_value = numbers[0]
    
    for num in numbers:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
           
    return (max_value, min_value)
   
# count_occurrences(items, target) — Takes a list and a target value, returns how many times the target appears in the list. Do NOT use the built-in .count() method.
def count(items, target):
    g =0
    for item in items:
        if item == target:
            g += 1
    return g

    


# is_palindrome(text) — Takes a string, returns True if it reads the same forward and backward (case-insensitive, ignoring spaces). Examples: "racecar" → True, "hello" → False, "A man a plan a canal Panama" → True.
def is_palindrome(text):
    # Clean the text first
    cleaned = text.lower().replace(" ", "")
    
    left = 0
    right = len(cleaned) - 1
    
    # Loop until the pointers meet in the middle
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False  # Found a mismatch!
        left += 1
        right -= 1
        
    return True  # Everything matched perfectly

# create_report(title, scores) — Takes a report title and a list of scores. Uses calculate_average and find_max_and_min internally. Returns a formatted string report (NOT a print — a return).
def report(title, scores):
    s = 0
    max = score[0]
    min = score[0]
    for ti, score in scores:
        s = s + score
        if score > max:
            max == score
        if score < min:
            min == score
    avg = s % len(scores)
    return avg, max, min
# Helper Function 1: Calculate the average
def calculate_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores)

# Helper Function 2: Find max and min
def find_max_and_min(scores):
    if not scores:
        return None, None
    
    maximum = scores[0]
    minimum = scores[0]
    
    for score in scores:
        if score > maximum:
            maximum = score  
        if score < minimum:
            minimum = score  
    return maximum, minimum

# Main Function: Creates and returns the formatted report
def create_report(title, scores):
    # Call the helper functions internally
    avg = calculate_average(scores)
    maximum, minimum = find_max_and_min(scores)
    
    # Generate a clean, formatted string report
    report_string = (
        f"--- {title} ---\n"
        f"Average Score: {avg:.2f}\n"
        f"Highest Score: {maximum}\n"
        f"Lowest Score:  {minimum}"
    )
    
    return report_string


    # Test each function
test_scores = [85, 92, 78, 95, 88, 70, 93]
    
print(f"Average: {calculate_average(test_scores)}")
print(f"Max/Min: {find_max_and_min(test_scores)}")
print(f"Count of 85: {count(test_scores, 85)}")
print(f"'racecar' palindrome: {is_palindrome('racecar')}")
print(f"'hello' palindrome: {is_palindrome('hello')}")
print()
print(create_report("Class Scores", test_scores))



     

# After defining all functions, add a test section:
