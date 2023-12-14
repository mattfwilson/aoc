my_list = [10, 20, 30, 40, 50]

for index, value in enumerate(my_list):
    # Print before each iteration
    print(f"Before - Index: {index}, Value: {value}")

    # Your main loop logic goes here
    result = value + 1
    print(f"Result - Index: {index}, Value: {value}, Doubled: {result}")

    # Print after each iteration
    print(f"After - Index: {index}, Value: {value}")

# Continue with other code after the loop
print("Loop completed.")
