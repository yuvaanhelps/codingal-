l=[5,4,6,3,2,8,1,7]
print("Original list:", l)
# variblr to store the sum of the list
count=0
#finding the sum
for i in l:
    count+=i
    # divide the total elements
avg=count/len(l)
print("sum=", count)
print("average=", avg)
    # sorting the  element of the list
l.sort()
#printing the first element
print("smallest element is:", l[0])
#printing the last element
print("largest element is:", l[-1])
