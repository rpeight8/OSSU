file_name = "9-4.txt"

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

maximum_email = None
maximum_number = None

for email, number in emails.items():
    if maximum_number is None or number > maximum_number:
        maximum_number = number
        maximum_email = email

print(maximum_email, maximum_number)
