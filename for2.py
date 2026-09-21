# for i in range(10,0,-1):
#     print(i)

# for i in range(1,11):
#     print(i)

# # 3rd question:

# for i in range(1,21):
#     if i % 2 == 0:
#         print(i)

# # 4th question:

# for i in range(1,21):
#     if i % 2 != 0:
#         print(i)

# # 5th question :

# count = 0 
# for i in range(1,11):
#     count = count + i 

# print(count)

# # 6th question :
# even_count = 0

# for i in range(1,21):
#     if i %2 == 0:
#         even_count = even_count + i 

# print(even_count)

# # 7th question :

# odd_count = 0

# for i in range(1,21):
#     if i % 2 !=0:
#         odd_count = odd_count + i

# print(odd_count)

# # 8th question:

# five_divisible_count = 0

# for i in range(1,51):
#     if i % 5 ==0:
#         five_divisible_count = five_divisible_count + 1

# print(five_divisible_count)

# 9th question:

# num = int(input("Enter a number to get that number multiplication : "))

# for j in range(1,21):
#     value = j * num
#     print(value)

# 10th question:

# for i in range(1,11):
#     value = i * i
#     print(value)

# 11th question:

# for i in range(1,11):
#     value = i * i * i 
#     print(value)

# 12 th question:

# count1 = 0 

# for i in range(1,101):
#     if i % 3 ==0 and i % 5 ==0:
#         count1 = count1 + 1

# print(count1) 

# 13 the question: 

# largest_value = 0

# numbers = [12, 45, 7, 89, 23, 56, 91, 34]

# for i in numbers:
#     if i > largest_value:
#         largest_value = i

# print(largest_value) 

# 14 th question :

# numbers = [12, 45, 7, 89, 23, 56, 91, 34 , 2]

# small_value= numbers[0]
# for i in numbers:
#     if small_value > i :
#         small_value = i

# print(small_value)

# 15th question:

# numbers = [10, 25, 30, 45, 50, 65, 70, 85]

# value = 40 
# count = 0 
# for i in numbers:
#     if i > value :
#         count = count + 1

# print(count)

# 16th question :
# numbers = [10, 15, 22, 30, 41, 50, 63, 72]

# sum = 0
# value = 40
# for i in numbers:
#     if i > value:
#         sum = sum + i 

# print(sum)

# 17th question:

# numbers = [10, 15, 22, 30, 41, 50, 63, 72]

# for i in numbers:
#     if i % 2 ==0 and i % 3== 0:
#         print(i)

# 18th question:

# numbers = [5, 12, 7, 20, 33, 40, 51, 60]

# count = 0

# for i in numbers:
#     if i % 3 ==0 and i % 2 !=0:
#         count = count + 1

# print(count)

# 19th question:
# numbers = [10, 25, 30, 45, 50, 65, 70, 85]
# average = 0
# for i in numbers:
#     average = average + i

# print(average / len(numbers))


# 20th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# for i in numbers:
#     if i > 10 and i %2 ==0:
#         print(i)

# 21th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]
# sum = 0 
# for i in numbers:
#     if i <=10:
#         sum = sum + i

# print(sum)

#22th question:
# numbers = [10, 15, 20, 25, 30, 35, 40, 45]
# count = 0
# for i in numbers:
#     if i>= 20 and i <= 40:
#         count = count + 1

# print(count)

# 23th question:
# numbers = [10, 25, 30, 45, 50, 65, 70, 85]

# new_list=[]

# for i in numbers:
#     if i > 40:
#         new_list.append(i)

# print(new_list)

# 24th question:
# numbers = [10, 25, 30, 45, 50, 65, 70, 85]

# new_squares=[]

# for i in numbers:
#     if i % 2==0:
#         square = i * i
#         new_squares.append(square)

# print(new_squares)

# 25th question:
# numbers = [10, 25, 30, 45, 50, 65, 70, 85]

# new_list = []

# for i in numbers:
#     if i % 5 ==0 and i % 10 !=0:
#         new_list.append(i)

# print(new_list)

# 26th question:
# numbers = [12, 7, 25, 30, 18, 41, 50, 9]
# new_list = []
# largest_num = 0
# for i in numbers:
#     if i > largest_num:
#         largest_num = i 
#         new_list.append(largest_num)

# print("Second Largest number : ",new_list[-2])

# 27th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# odd_list = []

# for i in numbers:
#     if i %2 !=0:
#         odd_list.append(i)

# print(odd_list)

#28th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# new_list = []

# for i in numbers:
#     if 2 % i == 0:
#         new_list.append(i)

# print(new_list)

# 29th question:

# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# odd_list = []

# for i in numbers:
#     if i % 2 !=0:
#         odd_square = i * i
#         odd_list.append(odd_square)

# print(odd_list)

# 30th question:

# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# even_list = []
# largest = 0
# for i in numbers:
#     if i % 2 ==0 and i > largest :
#         largest = i

# print(largest)    

# 31th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# small= numbers[0]

# for i in numbers:
#     if i %2 !=0 and i < small:
#         small = i

# print(small)

#32th question:

# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# odd_sum = 0

# for i in numbers:
#     if i % 2!=0:
#         odd_sum = odd_sum + i

# print(odd_sum)


#33th question:

# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# count = 0
# for i in numbers:
#     if i > 5 and i%2 !=0:
#         count = count + 1

# print(count)

#34th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# new_list = []

# for i in numbers:
#     if i % 3 !=0:
#         new_list.append(i)

# print(new_list)

# #35th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# new_list = []

# for i in numbers:
#     if i > 10 :
#         value = 3 * i
#         new_list.append(value)

# print(new_list)

#36th question:

# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# total = 0

# for i in numbers:
#     if i % 2 ==0:
#         value = i * i
#         total = value + total

# print(total) 


#37th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# odd_value = 0

# for i in numbers:
#     if i % 2 !=0 and i > odd_value:
#         odd_value = i

# print(odd_value)

#38th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# even_value = numbers[0]

# for i in numbers:
#     if i % 2 ==0 and i < even_value:
#         even_value = i

# print(even_value)

# 39th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# count = 0

# for i in numbers:
#     if i % 2==0 and i > 10 :
#         count = count + 1

# print(count)

#40th question:
# numbers = [12, 5, 8, 21, 7, 14, 3, 10]

# cubes_list = []

# for i in numbers:
#     if i % 2 ==0:
#         value = i * i * i
#         cubes_list.append(value)

# print(cubes_list)

