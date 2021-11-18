'''
1) We have discussed Binary search algorithm in the class. Implement the same algorithm using any of the languages like C/Python. Write all the possible testcases. Write down your observations. 
Sample input
Enter number of elements 8
Enter 8 elements
44,16,18,164,47,10,0,-68
Enter element to search 10
Sample output
10 is present at location 5
program:
'''
# Binary search
n = int(input("enter length of the array: "))
b = []
 
for i in range(n):
    p = int(input("enter element{}: ".format(i+1)))
    b.append(p)
    
#print("list: ",b)
key = int(input("enter the search element: "))
 
found = 0
high = n-1
low = 0
 
 
#print("values are: ",high,low,mid)
 
while low <= high and found == 0:
    
    mid = (high + low)//2
    
    if b[mid] == key:
        print(key,"is present at location ",mid)
        found = 1
        
    elif key < b[mid]:
        high = mid - 1
        
    elif key > b[mid]:
        low = mid + 1
    
'''
2) Once there lived a king and a queen. They were very rich and led a happy life. 
 The King's brother Humayun was jealous of him and he wanted to become the King. So in order to become the King, Humayun carries the Queen away and keeps her in a jail which are numbered in sorted sequence.
Humayun informs the King that he took away the Queen and if the King agrees him to become the King, he would leave the Queen. The King has a special power of flying. He flies and reaches the place where Humayun has hidden the Queen and Humayun has given clue to King about the jail number of the Queen. Luckily the King finds the key of the jail where the Queen is locked.But Humayun might have tried to fool the King by saying wrong jail number of Queen. The King already knew how many jails were there. He reaches the centre jail and checks whether the jail number and the key number are equal. He also carries a small machine with him to find the next jail to be visited by him. The machine initially contains the low(low=1) and the high value(high=total number of jails), and calculates the mid value (the jail which is to be visited). If the mid value and key value are equal, the King opens the lock and takes the Queen away with him. If the key number is greater than the mid value, the King increases the mid value by 1 in the machine and assigns it to the low value. If the key number is less than the mid value, the King decreases the mid value by 1 in the machine and assigns it to the high value. The King does this until he finds that the key value and the mid value to be equal.
 
program:
'''
# Binary search
n = int(input("Enter the total number of jails in Humayun's Place: "))
b = []
 
for i in range(n):
    p = int(input("enter jail number{}: ".format(i+1)))
    b.append(p)
    
#print("list: ",b)
key = int(input("Enter the clue given by Humayun: "))
 
found = 0
high = n-1
low = 0
 
while low <= high and found == 0:
    
    mid = (high + low)//2
    
    if b[mid] == key:
        #print(key,"is present at location ",mid)
        found = 1
        
    elif key < b[mid]:
        high = mid - 1
        
    elif key > b[mid]:
        low = mid + 1
        
if found!=0:
    print("Hurray!The King rescued the Queen")
else:
    print("The King has been fooled by Humayun")
 
'''
3) Given an Array A of N  of integers.You have to find number of subarrays having Primicity less than or equal to K 
Primicity of sub-array is defined an number of primes in that subarray.
Input:
First line contains N  and K
Second line contains N  integers.
Output:
Print the Number of sub-arrays having Primicity<= K 
'''
