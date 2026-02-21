# Roman numeral to Integer


def roman_to_int(s):
    roman_numerals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    value = 0
    i=0
    while i < len(s):
        if i+1 < len(s) and roman_numerals[s[i]] < roman_numerals[s[i+1]]:
            value += roman_numerals[s[i+1]] - roman_numerals[s[i]]
            i += 2
        else:
            value += roman_numerals[s[i]]
            i += 1
    return value


s= "MCMXCIV"
print(roman_to_int(s))

