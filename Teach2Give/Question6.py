vowels = "aeiouAEIOU"
def count_vowels(sentence):
  vowel_count = 0
  for char in sentence:
    if char in vowels:
      vowel_count += 1
  return vowel_count

# Example usage
sentence = "This is a test sentence."
vowel_count = count_vowels(sentence)
print(f"The sentence has {vowel_count} vowels.")