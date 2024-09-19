#Click Run to run the final project you will build.
#Welcome to the tip calculator!
#What was the total bill? $
#10
#How much tip would you like to give? 10, 12, or 15? 
#10
#How many people to split the bill?
#2
#Each person should pay: $5.50



print("Welcome to the tip calculator!")
total_conta = int(input("What was the total bill? "))

tip = int(input("How much tip would you like to give? 10, 12 or 15? "))

conta_tip = total_conta / tip + total_conta     
pessoas = int(input("How many people to split the bill? "))

total_por_pessoa = float(conta_tip / pessoas)
print("Each person should pay: ")
print(total_por_pessoa)
