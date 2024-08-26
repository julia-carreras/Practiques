print("Welcome to Hogwarts! "
      "The Sorting Hat is going to decide your House after some questions...")
free_time = input('''You have some free time. Where do you go? 
A. The Library 
B. The Great Hall
C. The Forbidden Forest
D. The Astronomy Tower
Type A, B, C or D \n''').upper()

money = input('''If you found a bag of Galleons on the ground, what would you do?
A. Return it to its right owner or leave it there.
B. Keep it to yourself but use it to help others in need.
C. Hand it over to the authorities.
D. Keep it to yourself and invest it in something beneficial.
Type A, B, or D \n''').upper()

animal = input('''If you could have any magical creature as a companion, which would you choose?
A. The wise Phoenix
B. The hard-working House-Elf
C. The mysterious Thestral
D. The protective Hippogriff
Type A, B, C, or D \n''').upper()

decision = input('''When faced with a difficult decision, what do you rely on the most?
A. The best outcome for you and those you care about 
B. Your sense of right and wrong
C. Your instincts
D. Logical reasoning
Type A, B, C or D \n''').upper()


artifact = input('''Which magical artifact would you most like to possess?
A. The Elder Want, for it's unbeatable power.
B. The Resurrection Stone, to connect with those who have passed.
C. The Invisibility Cloack, to move unseen and protect yourself and others.
D. The Maradeur's Map, to have knowledge of everyone's whereabouts.
Type A, B, C or D \n''').upper()

Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

if free_time == "A":
    Ravenclaw += 1
elif free_time == "B":
    Gryffindor += 1
elif free_time == "C":
    Slytherin += 1
elif free_time == "D":
    Hufflepuff += 1

if money == "A":
    Hufflepuff += 1
elif money == "B":
    Gryffindor += 1
elif money == "C":
    Ravenclaw += 1
elif money == "D":
    Slytherin += 1

if animal == "A":
    Ravenclaw += 1
elif animal == "B":
    Hufflepuff += 1
elif animal == "C":
    Slytherin += 1
elif animal == "D":
    Gryffindor += 1

if decision == "A":
    Slytherin += 1
elif decision == "B":
    Gryffindor += 1
elif decision == "C":
    Hufflepuff += 1
elif decision == "D":
    Ravenclaw += 1

if artifact == "A":
    Slytherin += 1
elif artifact == "B":
    Hufflepuff += 1
elif artifact == "C":
    Gryffindor += 1
elif artifact == "D":
    Ravenclaw += 1


if Gryffindor == Ravenclaw and Gryffindor != 0:
    duel = input('''You are in a duel with a wizard. What is your first move?
    A. Defend yourself and strategize your next move.
    B. Look for an opening to disarm them.
    Type A or B \n''').upper()
    if duel == "A":
        Ravenclaw += 1
    elif duel == "B":
        Gryffindor += 1

elif Gryffindor == Hufflepuff and Gryffindor != 0:
    duel_2 = input('''You are in a duel with a wizard. What is your first move?
    A. Look for an opening to disarm them.
    B. Call for help and try to negotiate a peaceful resolution.
    Type A or B \n''').upper()
    if duel_2 == "A":
        Gryffindor += 1
    elif duel_2 == "B":
        Hufflepuff += 1

elif Gryffindor == Slytherin and Gryffindor != 0:
    duel_3 = input('''You are in a duel with a wizard. What is your first move?
    A. Attack swiftly and aim to overpower them.
    B. Look for an opening to disarm them.
    Type A or B \n''').upper()
    if duel_3 == "A":
        Slytherin += 1
    elif duel_3 == "B":
        Gryffindor += 1

elif Ravenclaw == Hufflepuff and Ravenclaw != 0:
    duel_4 = input('''You are in a duel with a wizard. What is your first move?
    A. Call for help and try to negotiate a peaceful resolution.
    B. Defend yourself and strategize your next move.
    Type A or B \n''').upper()
    if duel_4 == "A":
        Hufflepuff += 1
    elif duel_4 == "B":
        Ravenclaw += 1

elif Ravenclaw == Slytherin and Ravenclaw != 0:
    duel_5 = input('''You are in a duel with a wizard. What is your first move?
    A. Attack swiftly and aim to overpower them.
    B. Defend yourself and strategize your next move.
    Type A or B \n''').upper()
    if duel_5 == "A":
        Slytherin += 1
    elif duel_5 == "B":
        Ravenclaw += 1

elif Hufflepuff == Slytherin and Hufflepuff != 0:
    duel_6 = input('''You're in a duel with a wizard. What is your first move?
    A. Attack swiftly and aim to overpower them.
    B. Call for help and try to negotiate a peaceful resolution.
    Type A or B \n''').upper()
    if duel_6 == "A":
        Slytherin += 1
    elif duel_6 == "B":
        Hufflepuff += 1

house_points = {
        'Gryffindor': Gryffindor,
        'Ravenclaw': Ravenclaw,
        'Hufflepuff': Hufflepuff,
        'Slytherin': Slytherin
    }
highest_house = max(house_points, key=house_points.get)

if ((Gryffindor == Ravenclaw and Gryffindor != 0) or
    (Gryffindor == Hufflepuff and Gryffindor != 0) or
    (Gryffindor == Slytherin and Gryffindor != 0) or
    (Ravenclaw == Hufflepuff and Ravenclaw != 0) or
    (Ravenclaw == Slytherin and Ravenclaw != 0) or
    (Hufflepuff == Slytherin and Hufflepuff != 0)):

    print("Maybe you're a Muggle after all... Answering all the questions could work a little magic...")

else:
    print(f"You're a {highest_house}!!!!")
