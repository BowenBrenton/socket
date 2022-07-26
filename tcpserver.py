import socket
import threading


IP = "111.111.11.1"
PORT = 8080

def main ():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((IP, PORT))
    server.listen(10)
    print(f'[*] Listening on {IP}:{PORT}')

    while True:
        client, addr = server.accept()
        print(f'[*] Accepted connection from {addr[0]}:{addr[1]}')
        client_handler = threading.Thread(target=handle_client, args=(client,))
        client_handler.start()

def handle_client(client_socket):
    with client_socket as sock:
        request = sock.recv(1024)
        print(f'[*] Received: {request.decode(utf-8)}')
        sock.send(b'ACK')

if __name__ == '__main__':
    main()

    
