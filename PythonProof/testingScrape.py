
sampleString = "Time until start: 12 minutes"

numbers = []
for word in sampleString.split():
    if word.isdigit():
        numbers.append(int(word))

print(numbers)
