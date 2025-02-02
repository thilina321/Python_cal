def calculator():
    try:
        expression = input("Enter calculation (e.g., 10 + 5 - 3 * 2 / 4): ")
        result = eval(expression)
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero")
    except Exception as e:
        print("Invalid input:", e)

calculator()

