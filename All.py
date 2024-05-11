

# Question 1 task:1 Code Correction
place = input("Choose a place (forest/cave?):")
action = input("Choose an action(climb a tree/cross a river?):")
if place == "forest":
 if action == "climb a tree":
    print("You found a bird's nest!")
elif action == "cross a river":
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
# Question 1 task:2 Setting the scene
place = input("Choose a place(forest/cave?):")
action = input("Choose an action(climb a tree/cross a river?):")
place = input("Choose a place(light a torch/proceed in the dark?):")
if place == "forest":
 if action == "climb a tree":
    print("You found a bird's nest!")
elif action == "cross a river":
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
elif place == "light torch":
    print("it is bright and you find a hidden treasure")
else:
    print("it is dark and you can not find a hidden treasure")

# Question 1 task:3 Defualt Path
user_preferance = input("Enter your preferance (Cave/Cross a river/Forest):")

if user_preferance == "Cave":
    print("Cave!")
elif user_preferance == "Cross a river":
    print("Cross a river!")
elif user_preferance == "Forest":
    print("Forest!")
else:
    pass

# Question 2 task:1 Code Correction

attendees = int(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room" 
print(venue)


# Question 2 task:2 Veneue Selection

attendees = int(input("Enter number of attendees:"))
venue = "large hall" if attendees > 100 else "conference room" if attendees > 75 else "audio system or projector"
print(venue)

# Question 2 task:3 Catering Choices

food = input("do you prefer veggie or non_veggie):")
if food == "veggie":
        print("Veggie Delight Caterers")
else:
        print("Gourmet Meals Caterers")
