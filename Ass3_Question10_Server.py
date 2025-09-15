import socket

HOST = '127.0.0.1'
PORT = 65432

def run_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.bind((HOST, PORT))
            s.listen()
            print("Server is listening for connections...")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                message = "Hello from server!"
                conn.sendall(message.encode('utf-8'))
        except socket.error as e:
            print(f"Socket error: {e}")

# Run bit
if __name__ == "__main__":
    run_server()