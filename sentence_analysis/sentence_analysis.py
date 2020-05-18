# Sentence Analysis Tool
"""
Write a script that takes a sentence from the user and returns:

- the number of lower case letters
- the number of uppercase letters
- the number of punctuations characters
- the total number of characters

Use a dictionary to store the count of each of the above.

**Note**: ignore all spaces.

Example input:
```
I love to work with dictionaries!
```

Example output:
```
Upper case: 1
Lower case: 26
Punctuation: 1
Total chars: 28
```
"""
import string

sentence = input(f'input a sentence: ')
results = {"upper case" : 0, "lower case" : 0, "punctuation" : 0, "total characters" : 0}
for letter in sentence:
    results["total characters"] += 1
    if letter.isupper():
        results["upper case"] += 1
        print(f"{letter} is upper case")
    if letter.islower():
        results["lower case"] += 1
        print(f"{letter} is lower case")
    if letter in string.punctuation:
        results["punctuation"] += 1
        print(f"{letter} is a punctuation")


print(results)