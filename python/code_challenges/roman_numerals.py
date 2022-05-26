# Start with a total of 0
# Start at the first character and repeat the steps until you reach the second to last character, one character at a time.
# The current character is left in the pair
# The following character is right in the pair
# Convert left and right characters to numbers
# If the left value is less than the right value then subtract the left value
# Otherwise, add the left value to the total
# Repeat as needed
# Convert the last character to a number
# Add to the total
# Return the total

def convert_character(roman_num):
    conversion = {
        "M": 1000,
        "D": 500,
        "C": 100,
        "L": 50,
        "X": 10,
        "V": 5,
        "I": 1
        }

    return conversion.get(roman_num,0)

def roman_numeral(num):

    arabic_num = 0

    for idx in range(len(num) - 1):

        left_num = num[idx]
        right_num = num[idx + 1]

        left_val = convert_character(left_num)
        right_val = convert_character(right_num)

        if left_val < right_val:
            left_val = -left_val

        arabic_num += left_val

    if num:
        arabic_num += convert_character(num[-1])

    return arabic_num

