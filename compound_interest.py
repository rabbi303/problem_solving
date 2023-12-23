def compound_interest(principles,rate,time):
 interest= principles*(1+(rate/100)*time)
 return interest

principles= int(input("Enter the principles amount :"))
rate= float(input("Enter the rate :"))
time= float(input("Enter the duartion of time :"))

interest_rate = compound_interest(principles,rate,time)
print("interest amount is :",interest_rate)
