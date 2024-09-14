def get_chinese_zodiac(year):
  
    zodiac_signs = ['Monkey', 'Rooster', 'Dog', 'Pig', 'Rat', 'Ox', 'Tiger', 
                    'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat']
    
    sign = zodiac_signs[year % 12]
    
    return sign

birth_year = int(input("Input your birth year: "))


zodiac_sign = get_chinese_zodiac(birth_year)

print(f"Your Zodiac sign: {zodiac_sign}")
