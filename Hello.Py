print ("Hello there! What is your name?")
name = input()

print ("Your name is " + name + "?" + " Yes/No")
yes = input()

if yes == "Yes":
    print ("Are you serious?" + " Yes/No")
    serious_answer = input()
    print ("Wow! That's a horrible name! You must live a hard life! Do you have a hard life?" + " Kinda/No")
        hard_life_answer = input()
        if hard_life_answer == "Kinda":
            print ("Yeah, I kinda thought so...")
elif serious_answer == "No":
    print ("You're NOT being serious? Yes/No")
    not_serious_answer = input()
    if not_serious_answer == "Yes":
        print ("Why so serious?")
    elif not_serious_answer == "No":
        print ("Bruh...")

    
        
        
else: print ("Why would you lie to me...")
