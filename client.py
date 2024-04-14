import socket
import threading
def receive_messages(client_socket):
    while True:
        message, _ = client_socket.recvfrom(1024)
    
        print("\nServer:", message.decode('utf-8'))
        client_socket.sendto(message.encode('utf-8'), ('localhost', 25252))    
        if message == "!QUIT":
            (exit)

def main():
    host = "localhost"  # Server IP
    port = 25252        # Server Port
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    while True:
        message = input("Enter your message to send: ")
        client_socket.sendto(message.encode('utf-8'), (host, port))

if __name__ == "__main__":
    main()
