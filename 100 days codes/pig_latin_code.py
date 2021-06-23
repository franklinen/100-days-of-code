try:
    engword = input("enter english word: ")
    if engword[0] in 'aeiou':
        print(f'{engword}way')
    else:
        print(f'{engword[1:]}{engword[0]}ay')
except ValueError:
    print(f'Hey thats not an English word')
        
        
        