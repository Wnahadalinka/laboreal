import re

def natural_sort_key(s):
    return [int(text) if text.isdigit() else text.lower()
            for text in re.split('([0-9]+)', s)]

# Example usage
variable1 = "apple10"
variable2 = "apple2"

sorted_variables = sorted([variable1, variable2], key=natural_sort_key)
print(sorted_variables)  # Output: ['apple2', 'apple10']
