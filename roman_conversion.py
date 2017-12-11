def romanToInt(s):
        
        numerals = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        counter = 0
        total = 0
        last_num = numerals[s[-1]]
        total += last_num
        while counter < len(s) - 1:
            next_num = counter + 1
            if numerals[s[counter]] < numerals[s[next_num]]:
                total -= numerals[s[counter]]
                counter += 1
            else:
                total += numerals[s[counter]]
                counter += 1

        return total

print(romanToInt("XXIX"))