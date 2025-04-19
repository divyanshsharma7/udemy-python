myDays=int(input("Enter the number of days :- "))
total=0
for i in range(1, myDays+1):
    nextDay=int(input("Enter the temperature of day "+str(i)+":- "))
    total=total+nextDay
average=total/myDays
print("Average temperature of given days is :- ",average)