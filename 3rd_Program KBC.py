questionsList=["In which country Mt Everest lies?", "What is the original name of Gautam Buddha?", "Who is the living legend?"]
answersList=["c", "d", "d"]
print("Welcome to the WHO WANTS TO BE A MILLIONAIRE")
print("Answer and win..All the Best!")
playon = True
while playon==True:
    print("So, Here's the first question for Re1 \n", questionsList[0])
    print("\n Your options are: \n a. United States \t b. Indonesia \n c. Nepal \t d. China")
    ans1=input()
    if (ans1==answersList[0]):
        print("Correct Answer!! \n ---Congratulations! You just won Re.1")
        playon=True

    else:
        print("Sorry, Incorrect Answer")
        playon=False
        break

    print("Here's the second question for Rs2 on your Computer Screen \n", questionsList[1])
    print("\n Your options are: \n a. Bikalpa Gautam \t b. Balbir Gautam \n c.Babbal Gautam \t d. Siddartha Gautam")
    ans2=input()
    if (ans2==answersList[1]):
        print("Correct Answer!! \n ---Congratulations! You just won Rs.2")
        playon=True

    else:
        print("Sorry, Incorrect Answer")
        playon=False
        break

    print("Well played, Here's the third question for Rs3 on your Computer Screen \n", questionsList[2])
    print("\n Your options are: \n a. Ramananda Paps \t b. Alien Musk \n c.Krishna Ronaldo \t d. Bikalpa KC")
    ans2=input()
    if (ans2==answersList[2]):
        print("Correct Answer!! \n ---Congratulations! You just won Rs.3")
        playon=False

    else:
        print("Sorry, Incorrect Answer")
        playon=False
        break
print("Thank you for playing, Nicely played. Paisa painna, it was just a prank ")



