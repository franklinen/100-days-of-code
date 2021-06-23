def mysum(*numbers):
    output = 0
    for number in numbers:
        output += number
    return output

mysum(3,4,6,7,8)

#Re-implement your mysum function such that it works in this way. If a second argument is not provided, then it should default to 0.
def mysum(numbers, n):
    return sum(numbers,n)

mysum([1,2,3], 4)

#Write a function that takes a list of numbers. It should return the average (i.e., arithmetic mean) of those numbers.
def mymean(numbers):
    sumnum = 0
    for i in numbers:
        sumnum += i
    avg = sumnum / len(numbers)
    return avg

mymean([1,3,5,6,7])

#Write a function that takes a list of words (strings). It should return a tuple containing three integers, representing the length of the shortest word, the length of the longest word, and the average word length.
def mystrings(words):
    wordlength = 0
    for word in words:
        x = len(max(words, key=len))
        y = len(min(words, key=len))
        wordlength = wordlength + len(word)
    avg = wordlength / len(words)
    return (x,y,avg)

mystrings(['come', 'go', 'here', 'belong'])


#Write a function that takes a list of Python objects. Sum the objects that either are integers or can be turned into integers, ignoring the others.
def sumint(*objects):
    suminter = 0
    for obj in objects:
        if obj == int(obj):
            suminter = suminter + obj
        else: suminter = suminter + 0
    return suminter

sumint(4, 5.0,3,21)
            
        
