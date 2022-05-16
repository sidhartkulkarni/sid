#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇


print('welcome to the tip calculator SK \n')
Bill = input("Enter your Bill amount: \n")
Bill = int(Bill)

tip= input("Tip you want to give 10% ,12%, 15% , 20% : \n")
tip=int(tip)
#print(tip)
tip_c=1+(tip/100)
#print(tip_c)

people= input("Enter no of people to split among : \n")
people = int(people)

total_amount = Bill*tip_c
#print(total_amount)

pax=total_amount/people
print(round(pax,2))
