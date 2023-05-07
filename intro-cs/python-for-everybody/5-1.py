largest = None
smallest = None
while True:
    s_num = input("Enter a number: ")
    if s_num == "done":
        break
    try:
        i_num = int(s_num)
    except:
        print("Invalid input")
        continue
    if largest is None or i_num > largest:
        largest = i_num
    if smallest is None or i_num < smallest:
        smallest = i_num

print("Maximum is", largest)
print("Minimum is", smallest)
