# Exercise 5: (Advanced) Change the socket program so that it only shows data after the headers and a blank line have been received. Remember that recv receives characters (newlines and all), not lines.
import socket

try:
    url = input("Enter URL: ")
    host = url.split("/")[2]
    my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    my_socket.connect((host, 80))
    cmd = f"GET {url} HTTP/1.0\r\n\r\n".encode()
    my_socket.send(cmd)

    loaded_data = ""
    while True:
        data = my_socket.recv(512)
        print(data)
        if len(data) < 1:
            break
        loaded_data += data.decode()
    my_socket.close()
    data_start_pos = loaded_data.find("\r\n\r\n") + 4
    print(loaded_data[data_start_pos : loaded_data.find("\r\n", data_start_pos)])
except:
    print("URL is invalid.")
    quit()
