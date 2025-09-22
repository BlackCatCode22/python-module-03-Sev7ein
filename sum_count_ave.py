#9/21/25

totalNumber = 0
totalCount = 0

while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    try:
        number = int(user_input)
        totalNumber += number
        totalCount += 1
    except ValueError:
        print("Invalid input, please enter an integer.")
#statement we recieve depends on if the fields were correctly answered
if totalCount > 0:
    average = totalNumber / totalCount
    print("Total:", totalNumber, "Count:", totalCount, "Average:", average)
else:
    print("No valid numbers were entered.")
