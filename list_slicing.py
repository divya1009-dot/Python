lst=[1, 5, 39, 126, 28, 27, 35, 1, 43, 24]
print("the original list is : ",lst)
counter=0
for i in lst:
    counter+=i
avr=counter/len(lst)
print('the avrage is :',avr)
print('the sum is',counter)
lst.sort()
print('the smallest element is',lst[0])
print("the biggest element is ",lst[-1])