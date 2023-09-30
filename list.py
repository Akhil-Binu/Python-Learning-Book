# a = [1,2,3,3,4,5,5,6,7,7,8,8]

# len1 = len(a)

# result = 0

# for i in range(len1):
#      for j in range(len1):
#         if(a[i]==a[j]):
#             break
#         else:
#           print(a[i])
            


# print(result)



# --------------------------------------------------------------------------------------------


# array = []
# size = int(input("Enter the size of array : "))
# print("Enter the elements in the array : ")
# for i in range(size):
#     a=int(input())
#     array.append(a)
  
# array2 = array
# print(array,array2)

# print("Enter the element to be added ")
# array2.append(int(input("Enter a number to be added : ")))

# print(array2)





# ----------------------------------------------------------------------

# # creating an empty list
# lst = []
 
# # number of elements as input
# n = int(input("Enter number of elements : "))
 
# # iterating till the range
# for i in range(0, n):
#     ele = int(input())
#     # adding the element
#     lst.append(ele) 
 
# print(lst)

 



# -----------------------------------------------------------------------------------------------

# array = []
# size = int(input("Enter the size of array  : "))
# for i in range(size):
#     element = int(input())
#     array.append(element)
# for i in range(size):
#     for j in range(size):
#         if(array[i]>array[j]):
#             temp = array[i]
#             array[i]= array[j]
#             array[j] = temp

# print('second largest element is ',array[1])


# --------------------------------------------------------------------------------


# def remove(duplicate):
#     final_list = []
#     for num in duplicate:
#         if num not in final_list:
#          final_list.append(num)
#     return final_list
# duplicate = [1,2,1,3,5,2,1]
# print(remove(duplicate))


# p = lambda x: x*x

# print(p(2))

# list1 = [1,2,3,4,5,6]
# # def even(x):
# #     if x % 2 == 0:
# #          return x
# # l = filter(even, list1)
# l = filter(lambda x: x%2 == 0, list1)
# print(list(l))


# function which return reverse of a string

# def isPalindrome(s):
# 	return s == s[::-1]


# # Driver code
# s = "malayalam"
# ans = isPalindrome(s)

# if ans:
# 	print("Yes")
# else:
# 	print("No")



def gen(x):
    yield 20
# k = lambda x : x+x 

# print(k(5))

# next(gen(10))
# class person:
#     def __init__(self):
#         self.ram =""
#         self.brand = ""

# a =person

# a.ram = "5gb"
# a.brand="dell"
# a.ram = "6gb"

list1 = [10,20,30,2,5]
largest = list1[0]
for i in list1:
    if(int(i)> largest):
        largest=list[i]

print(largest)



