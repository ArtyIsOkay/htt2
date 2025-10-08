confirm = 'y'

while confirm == 'y':
    age = int(input("Enter your age: "))
    if age < 1:
        print("The age must not be less than 1!")
    elif age >= 18:
        print("You are Adult")
    else:
        print("You are Child")
    confirm = input("To continue, enter 'y': ")
    