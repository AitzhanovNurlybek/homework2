
def print_O_pattern():
    height = 7
    width = 5
    
    for i in range(height):
        for j in range(width):
            
            if (i == 0 or i == height - 1) and (j != 0 and j != width - 1):  
                print('*', end='')
            elif (j == 0 or j == width - 1) and (i != 0 and i != height - 1):  
                print('*', end='')
            else:
                print(' ', end='')
        print()  

print_O_pattern()
