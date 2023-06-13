hour = int(input('Enter current hour : '))
time_of_day = input("am or pm: ")
future = int(input("How many hours ahead?;  "))
new_hour = (hour + future) % 12
if new_hour == 0:
    new_hour = 12
if time_of_day == 'am' and hour + future >= 12:
    time_of_day = 'pm'
elif time_of_day == 'pm' and hour + future >= 12 :
    time_of_day = 'am'
    time_of_day = 12
print(f"New hour : {new_hour} {time_of_day}")