# Fabonacci series

def fab(n):
    if n == 0 :
        return 0

    elif n == 1:
        return 1
    
    elif n== 2:
        return 1
    
    else:
        return fab(n-1)+fab(n-2)

for i in range(1):
    print(fab(i), end = ', ') 







# Function for nth Fibonacci number
def Fibonacci(n):
 
 # Check if input is 0 then it will
 # print incorrect input
   if n < 0:
       print("Incorrect input")
 # Check if n is 0
 # then it will return 0
   elif n == 0:
      return 0
 # Check if n is 1,2
 # it will return 1
   elif n == 1 or n == 2:
      return 1
   else:
      return Fibonacci(n-1) + Fibonacci(n-2)
