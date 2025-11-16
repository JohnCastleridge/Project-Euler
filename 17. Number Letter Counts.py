STOP = 1000


def spell_num(num: int) -> str:
    units  = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens  = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens   = ["ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
    powers = ["thousand", "million", "billion", "trillion", "quadrillion", "quintillion", "sextillion", "septillion", "octillion"]

    if num < 0:
        return "Minus" + " " + spell_num(-num).lower()

    digits = str(num)[::-1]

    if str(num) == "0":
        return "zero"
    
    word = ""
    if len(digits) > 3:
        for i in range(len(digits)//3+1):
            chunk = spell_num(int(digits[3*i:3*i+3][::-1]))
            if i == 0 and chunk != "zero":
                chunk = chunk[:-1]
            if i != 0:
                if word == "":
                    word = powers[i-1]  + word
                else:
                    word = powers[i-1] + " " + word
            if chunk != "zero":
                word = chunk + word
        return word.capitalize()

    start = 0
    if len(digits) >= 2 and digits[1] == "1":
        for digit in "0123456789":
            if digit == digits[0]:
                if word == "":
                    word = teens[int(digit)]+ word
                else:
                    word = teens[int(digit)] + " "+ word
                break
        start = 2
    
    for power in range(start, len(digits)):
        if power == 1 and digits[0] != "0":
            word = "-" + word
        elif power == 2:
            if digits[0:2] != "00":
                word = "and" + " " + word
            word = "hundred" + " " + word

        for digit in "123456789":
            if digit == digits[power]:
                if power == 1:
                    nums = tens
                else: 
                    nums = units
                if word and word[0] == "-":
                    word = nums[int(digit)-1] + word
                else:
                    word = nums[int(digit)-1] + " " + word
    return word


print(spell_num(110))

sum=0
for num in range(1, STOP+1):
    word = spell_num(num)
    word = word.replace(" ", "")
    word = word.replace("-", "")
    sum += len(word)
#print(sum)
