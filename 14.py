total_sum = 0
count = 0

while True:
    
    number = int(input())
    
    total_sum += number
    count += 1
    average = total_sum / count
    
    if number == 0:
        break
   
print(total_sum)
print(average)