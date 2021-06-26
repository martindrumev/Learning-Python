secret_world = "giraffe"
guess = ""
guess_list = []
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_world and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_list.append(guess)
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of guesses, YOU LOSE!")
else:
    print("You win!")
print()

guess_list.pop()
print("All wrong words: ")
print(guess_list)