def swapping(num1,num2):
    #now the swaping
    c = num2
    num2 = num1
    print("the variables of b and a are : {} and {}".format(c,num2))
num1 = int(input("Enter 1st variable :"))
num2 = int(input("Enter 2nd variable :"))

swap = swapping(num1,num2)

print("the variables of a and b are : {} and {}".format(num1,num2))


