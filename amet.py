def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as e:
        print(f"Error: Division by zero ({e})")
        raise  # Re-raise the original ZeroDivisionError

# Example usage
try:
    divide(5, 0)
except ZeroDivisionError:
    print("Caught the error raised from divide()")
