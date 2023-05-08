file_name = "9-4.txt"

try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

days = dict()

for line in file_handler:
    if line.startswith("From "):
        day = line.split()[2]
        days[day] = days.get(day, 0) + 1


print(dict(sorted(days.items(), key=lambda day: day[1], reverse=True)))
