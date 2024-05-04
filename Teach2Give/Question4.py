def capitalize_first_letters(text):
  # Split the string into words
  words = text.split()
  
  # Capitalize the first letter of each word
  capitalized_words = [word.capitalize() for word in words]
  
  # Join the capitalized words back into a string
  return " ".join(capitalized_words)

# Example usage
text = "i love programming"
capitalized_text = capitalize_first_letters(text)
print(capitalized_text)