# Initialize first two Fibonacci numbers
a, b = 0, 1

# Loop to print Fibonacci sequence up to 100
while a < 100:
  print(a, end=" ")
  a, b = b, a + b