hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
default_hours = 40
if hours > default_hours:
    overtime = hours - default_hours
    print(default_hours * rate + overtime * rate * 1.5)
else:
    print(hours * rate)
