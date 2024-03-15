def check_letter(letter):
    if letter.isupper():
        print("uppercase")
    elif letter.islower():
        print("lowercase")
        
    if letter.lower() in 'aeiou':
        print("vowel")
    else:
        print("consonant")


letter = input().strip()


check_letter(letter)