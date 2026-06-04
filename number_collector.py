
# ========================================
# Number 1 Input & Validation
# ========================================
try:
    num1 = int(input("Enter number 1: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num1 = 0

# ========================================
# Number 2 Input & Validation
# ========================================
try:
    num2 = int(input("Enter number 2: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num2 = 0

# ========================================
# Number 3 Input & Validation
# ========================================
try:
    num3 = int(input("Enter number 3: "))
except ValueError:
    print("That's not a valid number. Using 0 instead.")
    num3 = 0

# ========================================
# Calculations
# ========================================
total_sum = num1 + num2 + num3
average = total_sum / 3

# ========================================
# Display Results
# ========================================
print("\n" + "="*40)
print(f"Your numbers: {num1}, {num2}, {num3}")
print(f"Sum: {total_sum}")
print(f"Average: {average:.2f}")
print("="*40)