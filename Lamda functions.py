multiply= lambda x,y:x*y
def multiply2(fx, z):
    return (fx*z)


print("Enter two numbers")
n1=input("First number")
n2=input("Second number")
print("The product is:", multiply(int(n1),int(n2)))
choice= input("Want to multiply again? \n Enter: \n1. for yes \t 2. for no")
if int(choice)==int(1):
    n3=input("Enter the third number")
    print("The Final product is:", multiply2(multiply((int(n1),int(n2))), int(n3)))
else:
    exit()    
