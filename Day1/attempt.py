currSource = "test.txt"

attempt = open(currSource, "r")
line = attempt.readline()
sumOfNum = 0


while line:
    outputArray = []
    for i in line:
        if i.isnumeric():
            outputArray.append(i)
    print(outputArray)
    line = attempt.readline()

    

print(sumOfNum)
attempt.close()