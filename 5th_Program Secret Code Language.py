
import random


def Encoder(words):
    print("Encoding...")
    letters="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    for word in words:
        if (len(word)>2):
            randomletters1=str(random.choice(letters)) + str(random.choice(letters)) + str(random.choice(letters))
            randomletters2=str(random.choice(letters)) + str(random.choice(letters)) + str(random.choice(letters))
            finalword=randomletters1 + word[1:] + word[0]+ randomletters2
            print(finalword)

        else:
            finalword=word[::-1]
            print(finalword)


def Decoder(words):
    print("Decoding...")
    for word in words:
        if (len(word)>2):
            finalword=word[len(word)-4]+word[3:len(word)-4]
            print(finalword)
        else:
            finalword=word[::-1] 
            print(finalword)     

choice=input("Hi! Enter: \n 1. to Encode \t 2. to Decode \n")
if choice=="1":
    e="Encode"
else:
    e="Decode"
text=input(f"Enter the text to {e} \n")
words=text.split(" ")
if choice=="1":
    Encoder(words)
else:
    Decoder(words)    