
import socket

def tcp_server(host='127.0.0.1', port=12345):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
        server_socket.bind((host, port))
        server_socket.listen()
        print(f"TCP Server is listening on {host}:{port}")
        
        while True:
            conn, addr = server_socket.accept()
            print(f"Connected by {addr}")
            
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    print(f"Received: {data.decode()}")
                    conn.sendall(data)  # Echo the data back to the client

tcp_server()

