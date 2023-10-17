#python program to find the Factorial of a number using recursion 
#Fact_Recur.py 
def fact (m):
  if m<=1:
    return 1
  else:
    return m*fact (m-1)
#Main program 
n=int (input("Enter the value of n:"))
print ("The factorial of",n,"is",fact (n))