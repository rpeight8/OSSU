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

print(dict(sorted(emails.items(), key=lambda email: email[1], reverse=True)))
