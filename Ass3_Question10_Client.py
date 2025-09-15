import socket

HOST = '127.0.0.1'
PORT = 65432

def run_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((HOST, PORT))
            data = s.recv(1024)
            print(f"Received from server: {data.decode('utf-8')}")
        except socket.error as e:
            print(f"Socket error: {e}")

# Run bit
if __name__ == "__main__":
    run_client()