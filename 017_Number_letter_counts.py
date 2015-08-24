tens = {
    2: "twenty",
    3: "thirty",
    4: "forty",
    5: "fifty",
    6: "sixty",
    7: "seventy",
    8: "eighty",
    9: "ninety"
}

units = {
    0: "",
    1: "one",
    2: "two",
    3: "three",
    4: "four",
    5: "five",
    6: "six",
    7: "seven",
    8: "eight",
    9: "nine",
    10: "ten",
    11: "eleven",
    12: "twelve",
    13: "thirteen",
    14: "fourteen",
    15: "fifteen",
    16: "sixteen",
    17: "seventeen",
    18: "eighteen",
    19: "nineteen"
}


def write_number(n):
    output = ""
    if n >= 100:
        output += str(units[n / 100]) + "hundred"
        if n % 100 != 0: output += "and"
        n -= (n / 100)*100

    if n >= 20:
        output += str(tens[n / 10])
        n -= (n / 10)*10

    output += units[n]

    return output

total = 0
for i in range(1000):
    j = write_number(i)
    total += len(j)
    print j


print total
