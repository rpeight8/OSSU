import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen("http://data.pr4e.org/romeo.txt")

for line in fhand:
    # 3000 characters limit
    print(line.decode().strip()[:3000])
    print(f"Total characters: {len(line.decode())}")
