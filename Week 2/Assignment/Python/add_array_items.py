''' Task '''
#Given an array of integers,find the sum of its elements
# Sample Input arr=[1,2,3]
# Output = 1+2+3 returns 6

sum=0
my_arr = [1,2,10,8]

#Method 1
# for s in range(0,len(my_arr)):
# #     print(my_arr[s]
#       sum = sum + my_arr[s] 
# print(sum)


#Method 2
for x,n in enumerate(my_arr):
#  print(my_arr[x])
   sum= sum + my_arr[x]
print(sum) 

  