import socket

def udp_client():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server_address = ('localhost', 12345)

    message = input("Enter message to send: ")
    client_socket.sendto(message.encode(), server_address)
    data, _ = client_socket.recvfrom(1024)
    print(f"Received from server: {data.decode()}")

if __name__ == "__main__":
    udp_client()
