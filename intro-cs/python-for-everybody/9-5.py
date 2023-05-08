file_name = "9-4.txt"

try:
    file_handler = open(file_name)
except:
    print("File cannot be opened:", file_name)
    quit()

domains = dict()

for line in file_handler:
    if line.startswith("From "):
        domain = line.split()[1].split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

print(dict(sorted(domains.items(), key=lambda domain: domain[1], reverse=True)))
