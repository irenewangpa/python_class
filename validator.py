"""
Python Class

Example - Space Validator
"""

print('Program Started')

def calculate_efficiency(room_area, room_desk_count):
   efficiency = room_area / room_desk_count
   return efficiency
   
area = 100
desk_count = 4

result = calculate_efficiency(area, desk_count)

print(result)



# Create space dictionary
space = {
    'name',
    'area',
    'width',
    'is_occupied'
}
print (space)

# Create calculate_area
def calculate_area(width, height):
    area = width * height
    return area

width = 10
height = 20

print(calculate_area(width, height))
# same thing if you do this: print(calculate_area(10,20)) you can override the numbers

# Create make_upper_case
make_upper_case = 'abc'
print(make_upper_case.upper())

# Create validate_area
def validate_area(area):
    if area < 25:
        print('True')
    elif area > 25:
        print('False')

area = 30
print(validate_area(area))

# ^ Why does the word None print after False?

print('Program Ended')