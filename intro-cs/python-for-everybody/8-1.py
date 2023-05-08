fname = input("Enter a file name: ")
try:
    fhandler = open(fname)
except:
    print("File cannot be opened:", fname)
    quit()

words = list()

for line in fhandler:
    line = line.rstrip()
    for word in line.split():
        if word not in words:
            words.append(word)

words.sort()
print(words)
