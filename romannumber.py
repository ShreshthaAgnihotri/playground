#THIS PROGRAM IS TO CONVERT A GIVEN INTEGER INTO ROMAN NUMERAL BETWEEN 1 TO 3999


n = int(input("Enter a number between 1 and 3999: "))
if n<1 or n>3999:
    print("Invalid input")
else:
    val = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    rom = ['M', 'CM' ,'D' , 'CD' , 'C' ,'XC' , 'L' ,  'XL' , 'X' , 'IX' , 'V' , 'IV' ,'I']
    a=""
    for i in range (len(val)):
        while n>=val[i]:
            a+=rom[i]
            n-=val[i]
    print("The Roman numeral is: ", a)    
    