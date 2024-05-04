def reverse_digits(num):
  # Handle negative numbers by converting to positive, reversing, and making negative again
  if num < 0:
    return -reverse_digits(abs(num))
  
  reversed_num = 0
  while num > 0:
    # Extract the last digit
    digit = num % 10
    # Append the digit to the reversed number
    reversed_num = reversed_num * 10 + digit
    # Remove the last digit from the original number
    num //= 10
  return reversed_num

# Example usage
number = 12345
reversed_number = reverse_digits(number)
print(reversed_number)  # Output: 54321