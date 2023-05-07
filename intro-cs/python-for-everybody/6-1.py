text = "X-DSPAM-Confidence:    0.8475"
space_pos = text.find(" ")
number = float(text[space_pos:].strip())
print(number)
