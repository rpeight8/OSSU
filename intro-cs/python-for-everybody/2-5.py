scelsium = input("Enter t in Celcium: ")

try:
    icelsium = float(scelsium)
except:
    print("Invalid Celsium")
    exit()

print(icelsium * 1.8 + 32)
