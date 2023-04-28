def findStep(n):
    if ( n == 0 ):
        return 1
    elif (n < 0):
        return 0
    elif(n>30):
        return "Denied. Enter number less than or equal to 30"
    else:
        return findStep(n - 3) + findStep(n - 2) + findStep(n - 1)
 
n = int(input("Enter number of Steps : "))
print("Number of ways : ",findStep(n))