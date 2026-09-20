result = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
count = 0
for i in result:
    if i=='heads':
        count = count + 1

print("count of heads",count)


for i in range(10):
    if i %2 !=0:
        print(i*i)
 

for i in range(1,6):
    tired_message = input("You are tired? : ").lower()
    if tired_message == "yes":
        print("You didnt finish the race") 
        break
    elif tired_message =="no":
        if i == 5:
            print("Congratulations you won the race")
            continue

    
# Pattern Question:
for i in range(1,6):
    for j in range(1,6):
        if i>=j:
            print("*",end="")
        else:
            print(" ",end="")
    print(end="\n")

    





