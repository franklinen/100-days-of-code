word = input("Enter a word: ")

output = [ ]
for w in word:
    if w in 'aeiou':
        output.append(f'ub{w}')
    else:
        output.append(w)
print(''.join(output))