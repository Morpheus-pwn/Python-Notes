# Write a Python program to print the ASCII/Unicode value of characters, character to ascii

s=input("Enter a character: ")
print("The ASCII/Unicode value of", s, "is", ord(s))

# ascii number to character

s=input("Enter an ASCII/Unicode value: ")
print("The character corresponding to ASCII/Unicode value", s, "is", chr(int(s)))

# Print ASCII values of a word
word=input("Enter a word: ")
for char in word:
    print("The ASCII/Unicode value of", char, "is", ord(char))

# Print characters from ASCII values
start=int(input("Enter the starting ASCII/Unicode value: "))
end=int(input("Enter the ending ASCII/Unicode value: "))
for i in range(start, end+1):
    print("The character corresponding to ASCII/Unicode value", i, "is", chr(i))

# Write a program to check whether a character is uppercase using ASCII values.

s=input("Enter a character: ")
if(ord(s)>=65 and ord(s)<=90):
    print("The character", s, "is uppercase")
else:
    print("The character", s, "is not uppercase")

# Write a program to check whether a character is lowercase.

s=input("Enter a character: ")
if(ord(s)>=97 and ord(s)<=122):
    print("The character", s, "is lowercase")
else:
    print("The character", s, "is not lowercase")

# Write a program to check whether a character is a digit

s=input("Enter a character: ")
if(ord(s)>=48 and ord(s)<=57):
    print("The character", s, "is a digit")
else:
    print("The character", s, "is not a digit")

# Count uppercase letters

s=input("Enter a string: ")
count=0
for char in s:
    if(ord(char)>=65 and ord(char)<=90):
        count+=1
print("The number of uppercase letters in", s, "is", count)

# Count lowercase letters

s=input("Enter a string: ")
count=0
for char in s:
    if(ord(char)>=97 and ord(char)<=122):
        count+=1
print("The number of lowercase letters in", s, "is", count)

# Count digits
num=int(input("Enter a number: "))
count=0
while(num!=0):
    num//=10
    count+=1
print("The number of digits in", num, "is", count)

# Count separators comma,hyphen,semicolon.

s=input("Enter a string: ")
count=0
for char in s:
    if(char=="," or char=="-" or char==";"):
        count+=1
print("The number of separators in", s, "is", count)

# Write a program that checks whether the given character is a separator.
s=input("Enter a character: ")
if(s=="," or s=="-" or s==";"):
    print("The character", s, "is a separator")
else:
    print("The character", s, "is not a separator")

# Remove separators manually
# Eg: hello-world -> helloworld
s=input("enter a string: ")
word=""
for char in s:
    if(char=="," or char=="-" or char==";"):
        continue
    else:
        word+=char
print(word)


# Replace separators with spaces
s=input("enter a string: ")
word=""
for char in s:
    if(char=="," or char=="-" or char==";"):
        word+=" "
    else:
        word+=char
print(word)

# Convert sentence into list of words
s=input("enter a string: ")
words=[]
word=""
for char in s:
    if(char==" "):
        words.append(word)
        word=""
    else:
        word+=char
words.append(word)
print(words)

# Find the longest word
s=input("enter a string: ")
words=[]
word=""
for char in s:
    if(char==" "):
        words.append(word)
        word=""
    else:
        word+=char
words.append(word)
longest_word=words[0]
for word in words:
    if(len(word)>len(longest_word)):
        longest_word=word
print("The longest word in", s, "is", longest_word)

# Find the shortest word
s=input("enter a string: ")
words=[]
word=""
for char in s:
    if(char==" "):
        words.append(word)
        word=""
    else:
        word+=char
words.append(word)
shortest_word=words[0]
for word in words:
    if(len(word)<len(shortest_word)):
        shortest_word=word
print("The shortest word in", s, "is", shortest_word)

# Count words, digits and special characters
s=input("enter a string: ")
words=[]
word=""
for char in s:
    if(char==" "):
        words.append(word)
        word=""
    else:
        word+=char  
words.append(word)
count_words=0
count_digits=0
count_special_chars=0
for word in words:
    count_words+=1
    for char in word:
        if(ord(char)>=48 and ord(char)<=57):
            count_digits+=1
        elif((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)):
            continue
        else:
            count_special_chars+=1
print("The number of words in", s, "is", count_words)
print("The number of digits in", s, "is", count_digits)
print("The number of special characters in", s, "is", count_special_chars)

# Extract only numbers
s=input("enter a string: ")
nums=""
for char in s:
    if(ord(char)>=48 and ord(char)<=57):
        nums+=char
print("The numbers in", s, "are", nums)

# Extract only alphabets
s=input("enter a string: ")
alphabets=""
for char in s:
    if((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)):
        alphabets+=char
print("The alphabets in", s, "are", alphabets)

# Count each type of character
# Eg: input - Hello123!
#     output - 
# Uppercase: 1
# Lowercase: 4
# Digits: 3
# Special: 1

s=input("enter a string: ")
words=[]
word=""
for char in s:
    if(char==" "):
        words.append(word)
        word=""
    else:
        word+=char  
words.append(word)

count_digits=0
count_special_chars=0
count_uppercase=0
count_lowercase=0
for word in words:
    for char in word:
        if(ord(char)>=48 and ord(char)<=57):
            count_digits+=1
        elif((ord(char)>=65 and ord(char)<=90) or (ord(char)>=97 and ord(char)<=122)):
            continue
        else:
            count_special_chars+=1
for word in words:
    for char in word:
        if(ord(char)>=65 and ord(char)<=90):
            count_uppercase+=1
        elif(ord(char)>=97 and ord(char)<=122):
            count_lowercase+=1
print("The number of digits in", s, "is", count_digits)
print("The number of special characters in", s, "is", count_special_chars)
print("The number of uppercase letters in", s, "is", count_uppercase)
print("The number of lowercase letters in", s, "is", count_lowercase)  






