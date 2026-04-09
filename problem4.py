user_input = input("Enter your text: ")
with open("notes.txt","a") as file:
    file.write(user_input + "\n")

print("Your text has been saved")
