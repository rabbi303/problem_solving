#Floor division means the integer part of a division operation. For example, if you divide 17/5 the quotient will be 3.4.
def floor_division(num1,num2):
 result_floor= num1//num2 
 result_ceil= -(-num1//num2)
 return result_floor,result_ceil


num1=int(input("Enter the 1st number :"))
num2=int(input("Enter the 2nd number :"))

result_floor,result_ceil= floor_division(num1,num2)
print("The floor is :",result_floor)
print("The ceil is :",result_ceil)
