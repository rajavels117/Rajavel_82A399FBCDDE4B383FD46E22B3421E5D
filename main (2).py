a=int(input("Enter a year"))
if(a%400==0)and(a%100==0):
  print("It is a century year and also a leap year")
elif(a%4==0)and(a%100!=0):
  print("It is not a century year but it is a leap year")
else:
  print("It is not a leap year")