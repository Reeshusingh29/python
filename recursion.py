#recursion :- when a func call itself 
#factorial : 7*6*5*4*3*2*1
#n*n-1
def factorial(n):
   if(n==0 or n==1):
      return 1
   else:
        return n*factorial(n-1)


print(factorial(4))
   

#fibonacci number

def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fib_sequence = fibonacci(n - 1)
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
        return fib_sequence

# Fibonacci sequence ke pehle 10 terms ko print karein
result = fibonacci(3)
print(result)

