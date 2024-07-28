print("*** multiplication or sum ***")
num = input("Enter num1 num2 : ").split()
if int(num[1])*int(num[0]) > 1000:
    print(f"The result is {int(num[1])+int(num[0])}") 
else:
    print(f"The result is {int(num[1])*int(num[0])}") 