print("## Welcome to the guessing game... ")
name = input("# What is your name? ")
age = input("# What is your age?")
# age = int(input("What is your age?")) u dont need to put int one by one
health = 100
if int(age) >= 18:
    print("# Old enough to play this game :)")
    ready = input("# Do you want to play? (Yes/No) ").lower()
    if ready == "yes":
        print("Let's play", name, "!!!")
        print('# Here is the story !!')
        print("# You are starting with", health, "health")
# time count down
        import time
        t = 20
        def countdown(t):
            while t:
                mins, secs = divmod(t, 60)
                timer = '{:02d}:{:02d}'.format(mins, secs)
                print(timer, end="\r")
                time.sleep(1)
                t -= 1
            print("# One day bear going to his cave and he found a two ways to his cave.")
        countdown(int(t))
        left_or_right = input("# Which one you choose ? (Left / Right) :").lower()
        if left_or_right == "left":
            ans = input("# Nice..You follow the path and a reach a lake, Do you swim across or go around? (Around/Across) ").lower()
            if ans == "around":
                print("Here we go !!")
                ans = input("# You found a hive, You wanna bring it to home or leave it? (Bring/Leave)").lower()
                if ans == "bring":
                    print("# You got hitten by a bees, You lost",health - 50, "health")
                    ans = input("# You reached a cave, Are you give your hive to wife? (Yes/No) :")
                    if ans == "yes":
                        print("# Your wife give kiss and treat your wounds.your health restore back")
                        print("# You're current health", health, "You win!!")
                    else:
                        print("# Your wife going mad at you and kickoff you from home")

                else:
                    print("# Your wife kick out you home :( Game over!!")
            else:
                print("# You got killed by sharks :( Game over ..")

        else:
            print("# You fell into hell...Game over!! ")
    else:
        print("# Cya...come back later..")
elif int(age) >= 14:
    print("# You can play this game on supervision")
    print("# Have a nice day :)")
else:
    print("# You are not old enough to play this game :(")
    print("# Have a nice day:)")
