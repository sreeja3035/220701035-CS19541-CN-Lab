import socket

def udp_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_socket.bind(('localhost', 12345))

    print("UDP server is listening...")
    while True:
        data, client_address = server_socket.recvfrom(1024)
        print(f"Received from {client_address}: {data.decode()}")
        server_socket.sendto(data, client_address)  # Echo back the received data

if __name__ == "__main__":
    udp_server()
