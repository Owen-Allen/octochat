import socket

# https://realpython.com/python-sockets/
HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            data = conn.recv(1024)
            print(f"data: {data}")
            if not data:
                print('in break')
                break
            print("TIME TO SEND DATA")
            conn.send(data)


# first send, hello world
# second is hey i got it