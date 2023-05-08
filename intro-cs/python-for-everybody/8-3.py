numbers = []

while True:
    snumber = input("Enter a number: ")
    if snumber == "done":
        break

    try:
        inumber = int(snumber)
    except:
        print("Incorrect number")
        continue

    numbers.append(inumber)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
