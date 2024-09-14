def print_R_pattern():
    
    height = 7
    width = 5
    
    for i in range(height):
        for j in range(width):
            
            if j == 0 or (i == 0 or i == 3) and j < width - 1: 
                print('*', end='')
            elif j == width - 1 and (i != 0 and i != 3):  
                print('*', end='')
            elif i > 3 and i - j == 2:  
                print('*', end='')
            else:
                print(' ', end='')
        print()  


print_R_pattern()