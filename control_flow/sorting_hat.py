# Write code below 💖

gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

answer = int(
    input(
        """Q1) Do you like Dawn or Dusk?
    1) Dawn
    2) Dusk
    """
    )
)

if answer == 1:
    gryffindor += 1
    ravenclaw += 1
elif answer == 2:
    hufflepuff += 1
    slytherin += 1
else:
    print("Wrong answer")

answer = int(
    input(
        """Q2) When I'm dead, I want people to remember me as:
    1) The Good
    2) The Great
    3) The Wise
    4) The Bold
    """
    )
)

if answer == 1:
    hufflepuff += 2
elif answer == 2:
    slytherin += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong answer")

answer = int(
    input(
        """Q3) Which kind of instrument most pleases your ear?
    1) The violin
    2) The trumpet
    3) The piano
    4) The drum
    """
    )
)

if answer == 1:
    slytherin += 4
elif answer == 2:
    hufflepuff += 2
elif answer == 3:
    ravenclaw += 2
elif answer == 4:
    gryffindor += 2
else:
    print("Wrong answer")

if gryffindor > ravenclaw and gryffindor > hufflepuff and gryffindor > slytherin:
    print("GRYFFINDOR!")
elif ravenclaw > hufflepuff and gryffindor > slytherin:
    print("RAVENCLAW!")
elif hufflepuff > slytherin:
    print("HUFFLEPUFF!")
else:
    print("SLYTHERIN!")
