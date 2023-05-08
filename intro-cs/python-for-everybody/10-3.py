file_name = "10-1.txt"

try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

letters_periodicity = dict()

for line in file_handler:
    for letter in line:
        if letter.isalpha():
            letters_periodicity[letter] = letters_periodicity.get(letter, 0) + 1

for letter, number in sorted(
    letters_periodicity.items(), key=lambda letter: letter[1], reverse=True
):
    print(letter, ":", number)
