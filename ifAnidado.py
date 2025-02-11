age = int(input()) # Don't change this line
height = int(input()) # Don't change this line
has_adult = input() == "True" # Don't change this line

# Write your code below

if age >= 12:
    if height >= 150:
        if age < 15:
            if has_adult == "True":
                print("You can ride with adult supervision!")
            else:
                print("Sorry, you need an adult with you")
        else:
            print("You can ride by yourself!")
    else:
        print("Sorry, you're not tall enough")
else:
    print("Sorry, you're too young")               
