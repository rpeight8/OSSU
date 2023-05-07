def computepay(hours, rate):
    default_hours = 40
    if hours > default_hours:
        overtime = hours - default_hours
        return default_hours * rate + overtime * rate * 1.5
    else:
        return hours * rate


print(computepay(float(input("Enter Hours: ")), float(input("Enter Rate: "))))
