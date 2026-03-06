print ("Hello there! What is your name?")
name = input()
print ("Your name is " + name + "?" + " Yes/No")
yes = input()
if yes == "Yes":
    print ("Are you serious?" + " Yes/No")
    serious_answer = input()
    if serious_answer == "Yes":
        print ("Wow! That's a horrible name! You must live a hard life! Do you have a hard life?" + " Kinda/No")
        hard_life_answer = input()
        if hard_life_answer == "Kinda":
            print ("Yeah, I kinda thought so...")
else: print ("Why would you lie to me...")
