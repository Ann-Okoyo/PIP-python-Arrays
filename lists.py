# tuple_1=("Hello","Python",3.14,1.618,True,False,32,[1,2,3],{1,2,3},{'A':3,'B':8},(0,1))
# print(len(tuple_1))
# print(type(tuple_1))

nlis=["Python",25,2022]
nlis
print(nlis[0])
print(nlis[1])
print(nlis[-3])

Ann=["Hello","Python",3,14,2022]
len(Ann)
print(Ann[0:2])


Languages =["Python","Go language","Kotlin"]
Languages.extend(["JavaScript","CSS"])
Languages


school=["krs","Starch","AkiraChix"]
school1=school.append("Concord")
print(school1)

lis =[1,2,3,4,5]
print(len(lis))
print(max(lis))
print(min(lis))
lis.insert(7,8)


facts = ["smart","top","beautiful","Confident","lazy"]
del(facts[4])


smart = ["Ann",71,"Wakah","Omar"]
smart.extend(["smart","beautiful","intelligent"])
smart

Ann=["Mobile developer","Full stack developer","Engineer"]
Ann.append("musician")
Ann

Maths =[1,2,3,4,5,7]
print(len(Maths))
print(max(Maths))
print(sum(Maths))

# Write a Python program to find the 
# largest and smallest elements in an array.

work = [71,80,90,46,17,71]
print(max(work))
print(min(work))

# Write a Python program to find the
# second largest element in an array.
def num(num1):
    sorted = num1.sort()
    print(num1[-2])  

num([3,2,8,67,4])




# Write a Python program to remove 
# all the duplicates from an array. 
def removeDup(number):
    return list(set.numbers)

#  Write a Python program to find the
# sum of all the elements in an array.                                                                   
numbers =[90,89,78,68,90]
print(sum(numbers))