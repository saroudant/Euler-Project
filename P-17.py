"""NUMBER LETTER COUNTS Problem 17
First I create a function that writes the number (recursively to go quicker)
Then I concatenate all the integers between 1 and 1000.
Finally I take the length of this string """

def write_numbers(b):
    
    units = ['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen','nineteen']
    dozen_scale = ['ten','twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']

    if b < 20:
        return units[b]
    elif b < 100:
        return dozen_scale[b//10-1] + write_numbers(b%10)
    elif b < 1000:
        if b % 100 == 0:
            return write_numbers(b // 100) + "hundred"
        else:
            return write_numbers(b // 100) + "hundredand"+ write_numbers(b % 100)
    elif b == 1000:
        return "onethousand"

s = ""
mx = 1000

for i in range(1,mx+1):
    s += str(write_numbers(i))

print len(s)
