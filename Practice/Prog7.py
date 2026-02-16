m = int(input("Enter:"))
n = int(input("Enter:"))
l = [x for x in range(m, n+1)]
print("The average of the list is:",sum(l)/len(l))
print("The largest element in the list is:",max(l))