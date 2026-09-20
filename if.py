# india = ["mumbai", "banglore", "chennai", "delhi"]
# pakistan = ["lahore","karachi","islamabad"]
# bangladesh = ["dhaka", "khulna", "rangpur"] 

# Write a program that asks user to enter a city name and it should tell which 
# country the city belongs to

india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"] 

city = input('Enter a city name : ')
if city in india or pakistan or bangladesh:
    if city in india:
        print("india")
    elif city in pakistan:
        print("pakistan")
    elif city in bangladesh:
        print("bangladesh")
else:
    print("The entered city is not a valid")


city1 = input("Enter the first city name : ").lower()
city2 = input("Enter the second city name : ").lower()

if city1 in india and city2 in india:
    print("Both cities are in India")
elif city1 in pakistan and city2 in pakistan:
    print("Both cities are in pakistan")
elif city1 in bangladesh and city2 in bangladesh:
    print("Both cities are in bangladesh")
else:
    print("They dont belong to same country")



sugar_fasting_level = float(input("Enter your sugar fasting level : "))

if sugar_fasting_level <=80 :
    print("Sugar is low")
elif sugar_fasting_level >=100:
    print("Sugar is high")
else:
    print("Sugar is Normal") 
 
    




