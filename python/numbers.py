exercise_1 = "Exercise 1: write addition, subtraction, multiplication, and division operations that each result in the number 8."
print(exercise_1)

addition = 5 + 3
message = "The result of 5 + 3 is " + str(addition)
print(message)

subtraction = 18 - 10
message = "The result of 10 - 8 is " + str(subtraction)
print(message)

multiplication = 8 * 1
message = "The result of 8 * 1 is " + str(multiplication)
print(message)

division = 64 / 8
message = "The result of 64 / 8 is " + str(division)
print(message)

exercise_2 = "Exercise 2: Store your favorite number in a variable, then create a message that reveals your favorite number."
print(exercise_2)

while True:
    fav_number = input("What's your favorite number? ")
    if fav_number.isdigit():  # Checks if the input consists only of digits
        break  # Exits the loop if input is valid
    else:
        print("Oops! Please enter a valid number.")

print(f"That's so cool! {fav_number} is also my favorite number.")


#o exercicio era para ser mais simples, mas me empolguei e acabei colocando if else e while statements.