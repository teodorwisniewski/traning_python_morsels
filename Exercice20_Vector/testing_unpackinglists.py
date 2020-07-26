
import datetime
import sys
from collections import Counter

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

numbers = [1, 2, 3, 4, 5, 6,2,2,2,2,3,3,1,7,888,8,8,8,9,15,4,66,6,6,6,8]
letters = "abcdef"
first, *middle, last_one = numbers
print(first)
print(middle)
print(last_one)

random_data = ["red", [1,50,77]]
 #deep unpacking
color, (id1,id2,id3) = random_data 
print(color)
print(id1)
print(id2)
print(id3)

# more readable version of "deep unpacking"
(color, (x, y, z)) = ("red", (1, 2, 3))

start_points = [(1, 2), (3, 4), (5, 6)]
end_points = [(-1, -2), (-3, 4), (-6, -5)]

for (x1, y1), (x2, y2) in zip(start_points, end_points):
    if x1 == -x2 and y1 == -y2:
        print(f"Point {x1},{y1} was negated.")


for el in enumerate(zip(numbers,letters)):
    print(el)


for index, (number,letter) in enumerate(zip(numbers,letters)):
    print("index is " +str(index))
    print('letter is ' + letter)
    print('number is ' +str(number))


for (x1, y1), (x2, y2) in zip(start_points, end_points):
    if x1 == -x2 and y1 == -y2:
        print(f"Point {x1},{y1} was negated.")


just_checking = Counter(numbers).most_common(1)
# un packig a list of 1 tuple to one tuple o tuples
# deep inpucking
(value, times_seen), = just_checking
print(just_checking)
print(type(just_checking))
print(times_seen)

just_checking2 = Counter(numbers).most_common(1)
((value2,times_seen2),) = just_checking2
[(value3,times_seen3)] = just_checking2
print(  ((value,times_seen),) == tuple([(value2,times_seen2)])   )
print(  [((value,times_seen),)] == [(value2,times_seen2),]   )