def Fact(x):
  if x == 1:
    return 1
  else:
    print(x)
    sum = x*Fact(x - 1)
    return (sum)
num = int(input("Enter a number:"))
if num>= -1:
  print("Factorial value",Fact(num))
