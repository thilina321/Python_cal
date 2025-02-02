def calculator():
    numbers = list(map(float, input("Enter numbers separated by space: ").split()))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == "+":
        result = sum(numbers)
    elif operation == "-":
        result = numbers[0] - sum(numbers[1:])
    elif operation == "*":
        result = 1
        for num in numbers:
            result *= num
    elif operation == "/":
        result = numbers[0]
        for num in numbers[1:]:
            if num == 0:
                print("Error: Division by zero")
                return
            result /= num
    else:
        print("Invalid operation")
        return

    print("Result:", result)

calculator()
