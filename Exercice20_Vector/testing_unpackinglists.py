
import datetime
import sys

arguments = sys.argv
filename, *the_rest = sys.argv

today_date = str(datetime.date.today())

print(today_date)
print(type(today_date))

splitted_date = today_date.split("-")
year,month,day = splitted_date

print(f"It is {year}. The day is {day} and the month is {month} ")

# Conclusion: we can unpack lists! It is more readable than spllited_date[0] and so on!
print(arguments)

print(f"This is filename {filename}")
print(f"The rest of arguments  {the_rest}")

numbers = [1, 2, 3, 4, 5, 6]

first, *middle, last_one = numbers
print(first)
print(middle)
print(last_one)
