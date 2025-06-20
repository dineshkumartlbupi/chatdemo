
# problem two  sum using function
def sumtwonumber(lst,target):
    for i in range(len(lst)):
        for j in range(i+1,len(lst)):
            if lst[i]+lst[j]== target:
                return [i,j]
    return []


lst=[1,2,3,4,5,6,7,8]
target=8
result=sumtwonumber(lst,target)
print(result)



#problem two sum brute force
# lst=[1,2,3,4,5,6]
# target=10
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if lst[i]+lst[j]==target:
#             print("Pair found:",lst[i],lst[j])
