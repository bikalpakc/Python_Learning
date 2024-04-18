def fibonacci(n):
  if n == 0:  # base case
    return 0
  elif n == 1:  # base case
    return 1
  else:
    return fibonacci(n-1) + fibonacci(n-2)  # recursive call

# Print out the Fibonacci sequence up to the 10th term
for i in range(10):
  print(fibonacci(i))