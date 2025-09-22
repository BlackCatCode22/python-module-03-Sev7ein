# 9/21/25
#s.n

#code from exercise 6.5
str = 'X-DSPAM-Confidence: 0.8475'
# find the colon
ipos = str.find(':')
# slice after the colon
piece = str[ipos+1:]
# clean + convert to float
value = float(piece.strip())
print("Parsed value:", value)

numbers = []

while True:
    x = input("Enter a number (or 'done'): ")
    if x == "done":
        break
    try:
        num = float(x)
        numbers.append(num)
    except:
        print("Error")

if numbers:
    print("Maximum:", max(numbers))
    print("Minimum:", min(numbers))
else:
    print("No numbers entered.")
