try:
    fhandle = open(input("Enter file name: "))
except:
    print("Invalid file name")
    quit()

SPAM_STRING = "X-DSPAM-Confidence:"
spam_average = 0.0
spam_amount = 0
for line in fhandle:
    if line.startswith(SPAM_STRING):
        space_pos = line.find(" ")
        number = float(line[space_pos:].strip())
        spam_average += number
        spam_amount += 1

print("Average spam confidence:", spam_average / spam_amount)
