num = int(input("Input a number: "))
next_num = 1


while next_num <= 10:
    res = num * next_num
    print(f"{num} x {next_num} = {res}")
    next_num += 1
