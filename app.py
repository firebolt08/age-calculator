enteredAge = input("Please enter your age: ")
enteredAge.strip()
numAge = int(enteredAge)
if numAge < 18:
    print("You are a minor.")
elif numAge >= 18:
    print("You are an adult.")
