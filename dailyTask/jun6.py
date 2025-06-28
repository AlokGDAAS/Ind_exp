print("Press A for sum")
print("Press B for subtraction")
print("Press C for multiply")
print("Press D for division")

num1 = int(input("Enter First number : "))
num2 = int(input("Enter Second number : "))

calculation = input("Enter your calculation option: ")

calculation = calculation.upper()



if calculation == "A":
  print(num1 + num2)
elif calculation == "B":
  print(num1 - num2)
elif calculation == "C":
  print(num1 * num2)
elif calculation == "D":
  print(num1 / num2)
else:
  print("You have entered a wrong choice")