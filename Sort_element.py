# Sorting elements in the list

mylist  = [4,3,9,7,5]

for i in range (len(mylist)):
    for j in range(i+i,len(mylist)):
        if mylist[j] < mylist [i]:
            mylist[i],mylist[j] = mylist[j],mylist[i]
print(mylist)



# Sort list in accending 

mylist = [2,5,7,8,9]
   
new = sorted(mylist)
print(mylist)


# sort list in decending order

mylist =[2,5,7,8,9]
new = sorted(mylist,reverse = True)
print(new)