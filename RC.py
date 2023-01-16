name = input("Enter your name: ")
print("Hello" + name + "!")
age = input("How old are you? ")
print("Wow... You don't look " + age + ". Good job tricking time!")
fullname = input("Wait, what is your full name again? ")
print("You are THE " + fullname + "!? I hear you are THE BESTEST EVER OF THE SWEETS AND PRECIOUSHNESSES <3!")
girlfriend = input("By any chance, do you have a girlfriend?")

if girlfriend == "yes":
    print("Well you are so lucky, I hear she's great!")
elif girlfriend == "no":
    print("Then find one! Preferably in your current household!")
else:
    answer = input("Quit talking gibberish, I need a clear answer! Yes or No?")

if answer == "yes":
    print("Well you are so lucky, I hear she's great!")
elif answer == "no":
    print("Then find one! Preferably in your current household!")
