ph = int(input("Type a pH value (0-14): "))

if ph > 7:
    print("Basic")
elif ph < 7:
    print("Acidic")
else:
    print("Neutral")
