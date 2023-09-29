a = [1,2,3,3,4,5,5,6,7,7,8,8]

len1 = len(a)

result = 0

for i in range(len1):
     for j in range(len1):
        if(a[i]==a[j]):
            break
        else:
          print(a[i])
            


print(result)