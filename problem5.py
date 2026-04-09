def even_numbers(n):
    if n < 0:
        raise ValueError("Please enter a positive number")

    for i in range(0, n + 1):
        if i % 2 == 0:
            yield i

try:
    user_input = int(input("Enter a number: "))

    print("Even numbers are:")
    for list in even_numbers(user_input):
        print(list)

except ValueError as error:
    print(error)
