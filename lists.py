monthlyexpense = [{"january" : 2000},{"February" :2350},{"march" : 2600},{"April" : 2130},{"May" : 2190}]

spent_extra_money = monthlyexpense[1]["February"] - monthlyexpense[0]["january"]
print("This is the total dollars i spent extra compare to january : ",spent_extra_money)

for i in monthlyexpense:
    if (list(i.values())[0]) == 2000:
        print("This is the month i spent excetly : ",(list(i.keys())[0]))
        
monthlyexpense.append({"June" :1980})
print(monthlyexpense)

monthlyexpense[3]["April"] = monthlyexpense[3]["April"] - 200
print(monthlyexpense)

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append("black panter")

print(heros)

heros.pop()
heros.insert(3,"black panter")
print(heros)

del heros[1:3]
print(heros)

heros.sort()
print(heros)
