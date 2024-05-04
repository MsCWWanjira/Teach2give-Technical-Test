def is_power_of_two(n):
  if n <= 0:
    return False
  while n != 1:
    if n % 2 != 0:
      return False
    n //= 2
  return True

# Example usage
number = 16
if is_power_of_two(number):
  print(f"{number} is a power of two")
else:
  print(f"{number} is not a power of two")