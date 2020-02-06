"""roman_integer
Roman numeral to integer, integer to roman numeral
"""

specials = {4: "IV", 9: "IX", 40: "XL", 90: "XC", 400: "CD", 900: "CM"}
normals = {1: "I", 5: "V", 10: "X", 50: "L", 100: "C", 500: "D", 1000: "M"}
roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}


def doStage(stage, multi):
    roman_int = ""
    half = 5 * multi
    if stage * multi in specials:
        roman_int = roman_int + specials[stage * multi]
    elif stage * multi in normals:
        roman_int = roman_int + normals[stage * multi]
    elif stage * multi > half:
        roman_int = (
            roman_int
            + normals[half]
            + (normals[multi] * ((stage * multi - half) // multi))
        )
    elif stage * multi < half:
        roman_int = roman_int + (normals[multi] * ((stage * multi) // multi))

    return roman_int


def intToRoman(self, num: int) -> str:
    thousands = num // 1000
    hundreds = (num - thousands * 1000) // 100
    tens = (num - thousands * 1000 - hundreds * 100) // 10
    units = num - thousands * 1000 - hundreds * 100 - tens * 10
    roman_int = ""
    if thousands * 1000 in normals:
        roman_int = normals[thousands * 1000]
    else:
        roman_int = normals[1000] * thousands

    roman_int = roman_int + self.doStage(hundreds, 100)
    roman_int = roman_int + self.doStage(tens, 10)
    roman_int = roman_int + self.doStage(units, 1)
    return roman_int


def romanToInt(self, string):
    total = 0
    for i in range(len(string) - 1):
        cur = roman_dict[string[i]]
        if roman_dict[string[i + 1]] > cur:
            total -= cur
        else:
            total += cur
    total += roman_dict[string[-1]]
    return total


if __name__ == "__main__":
    print(doStage(4, 100))
