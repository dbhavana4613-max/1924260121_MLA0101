text =input("Enter a sentence:")
for ch in text:
    if ch.lower() in "aeiou":
        print(ch,"is a vowel")
