sumrun = 0
numrun = 0
while True:
    try:
        runtime = input("Enter 10km run time, or 'q' to exit: ")
        
        if runtime == 'q':
            break
        else:
            sumrun += float(runtime)
            numrun += 1
            avgtime = sumrun/numrun
            print(f'Average of {avgtime}, over {numrun} runs')
    except ValueError:
        print("Hey! That's not a valid number!")




s= 0.1 + 0.2
print(f'{s:.2f}')



def bea(x, before, after):
    
    

