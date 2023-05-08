file_name = "10-1.txt"

try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

emails = dict()

for line in file_handler:
    if line.startswith("From "):
        email = line.split()[1]
        emails[email] = emails.get(email, 0) + 1

sorted_by_number = sorted([(v, k) for (k, v) in emails.items()], reverse=True)

print(sorted_by_number[0])
