file_name = "10-1.txt"

try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

hours = dict()

for line in file_handler:
    if line.startswith("From "):
        hour = line.split()[5].split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1

for hour, number in sorted([(value, hour) for (hour, value) in hours.items()]):
    print(number, hour)
