#collections: arrays, lists, tuples
#contain or manage multiple items

#tuples is read only, immutable, uses (), takes less memory and sometime faster in access
#list:mutable, you can modify, uses []


#----------------Tuple---------------
# persons = ("Brian","Bob", "Alice", "Jean" )
# #loop
# #print(len(persons))
# #print last element
# #print(persons[-1])

# #print tuple
# #print(persons[2])

# # for i in range(0, len(persons)):
# #     print(persons[i])
# for i in persons:
#     print(len(i))
#     print(i)
#     print()
#     #print first letter of string 
#     print(i[0])
#     #print last letter
#     print(i[-1])
    
#variations
#values = range(0,5) same as (0,1,2,3,4)

#-----------------Lists-------------

# persons = ["Brian","Bob", "Alice", "Jean" ]
# #add to list
# new_person = "David"
# #or
# persons[0] = "Steven"

# #delete item
# del persons[1]

# persons.append(new_person)
# print(persons)

# #list is not a value, its a container: 
# def change_value(a):
#     a[0] = 10

# test = [1, 2, 3, 4]
# print(test)
# change_value(test)
# print(test)


#--------------Functions and Tuples-------------


#return multiple functions
# def get_information():
    
#     return "Alice", 20, 1.6

# def display_information(name, age, height):
#     print(f"Name: {name}, Age: {age}, Height: {height}")

# # info = get_information()
# # print(info)

# # print("Name: " + info[0])
# # print("Age: " + str(info[1]))
# # print("Height: " + str(info[2]) + "m")

# #alternative
# #name, age, height = get_information()
# # print(f"Name: {name}, Age: {age}, Height: {height}")

# #alternative 2
# # name, age, height = get_information()
# # display_information(name, age, height)

# #alternative 3
# info = get_information()
# print(info)
# display_information(*info) #unpack tuple with *



#----------------Slice-----------------
persons = ('Brian', "Bob", "Alice", "Jean", "Steve", "John")

#print(persons)
#syntax = [start:stop:step]
for i in persons[0:2]:  #print only first 2
    print(i)
    
#works for strings:
name = "Alice"
print(name[::-1])
    
