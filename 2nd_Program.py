import time
currentSystemHour= int(time.strftime("%H"))
# print (currentSystemHour)
if (currentSystemHour<12):
    print("Goodmorning Bikalpa!")
elif(currentSystemHour>=12 and currentSystemHour<17):
    print("Goodafternoon Bikalpa!")

elif(currentSystemHour>16 and currentSystemHour<21):
    print("Goodevening Bikalpa!")
else:
    print("Goodnight Bikalpa!")