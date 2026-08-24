#THIS PROGRAM IS TO FIND NO OF EVEN , ODD AND ZEROES IN GIVEN NUMBER

n = int(input("ENTER A NUMBER:"))
oddcount = 0
evencount = 0
zerocount = 0
while n>0:
    digit = n%10
    if digit%2 == 0 and digit!=0:
        evencount+=1
    elif digit%2 == 1:
        oddcount+=1
    elif digit ==0:
        zerocount+=1
    n = n//10
print("Number of even digits are : " ,evencount)     
print("Number of odd digits are : " ,oddcount)     
print("Number of zeroes are : " ,zerocount)     

   

        

