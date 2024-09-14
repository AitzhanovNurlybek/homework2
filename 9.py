def get_season(month, day):

    if (month == 12 and day >= 21) or (1 <= month <= 2) or (month == 3 and day < 20):
        return "winter"
    elif (month == 3 and day >= 20) or (4 <= month <= 5) or (month == 6 and day < 21):
        return "spring"
    elif (month == 6 and day >= 21) or (7 <= month <= 8) or (month == 9 and day < 22):
        return "summer"
    elif (month == 9 and day >= 22) or (10 <= month <= 11) or (month == 12 and day < 21):
        return "autumn"


month = int(input("Input the month (e.g. [1-12]): "))
day = int(input("Input the day: "))


season = get_season(month, day)

months = ["January", "February", "March", "April", "May", "June", 
          "July", "August", "September", "October", "November", "December"]

print(f"{months[month-1]}, {day}. Season is {season}.")
