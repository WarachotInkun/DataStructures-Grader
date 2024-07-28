class translator:

    def deciToRoman(self, num):
        values = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        symbols = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        roman = ""      
        for i, value in enumerate(values):
            while num >= value:
                roman += symbols[i]
                num -= value
        return roman
    def romanToDeci(self, s):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev_value = 0
        
        for char in reversed(s):
            current_value = roman_values[char]
            if current_value >= prev_value:
                result += current_value
            else:
                result -= current_value
            prev_value = current_value
        
        return result

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))

print(translator().romanToDeci(translator().deciToRoman(num)))