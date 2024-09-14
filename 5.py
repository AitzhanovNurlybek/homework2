
list_of_month = ["January", "February", "March", "April", "May", "June", "July", "August", 
                 "September", "October", "November", "December"]


name_of_month = input("Input the name of Month: ").capitalize()


if name_of_month in list_of_month:
    if name_of_month == "February":
        print("28/29 days")
    elif name_of_month in ["April", "June", "September", "November"]:
        print("30 days")
    else:
        print("31 days")
