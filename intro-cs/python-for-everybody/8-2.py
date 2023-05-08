fname = input("Enter a file name: ")
try:
    fhandler = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

emails = list()

for line in fhandler:
    if line.startswith("From "):
        emails.append(line.split()[1])

print(emails)
print("There were", len(emails), "lines in the file with From as the first word")
