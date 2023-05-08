import socket

try:
    url = input("Enter URL: ")
    host = url.split("/")[2]
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, 80))
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
    my_socket.send(cmd)

    while True:
        data = my_socket.recv(512)
        if len(data) < 1:
            break
        print(data.decode(), end="")

    my_socket.close()
except:
    print("URL is invalid.")
    quit()
