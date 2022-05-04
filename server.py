import socket
import threading
import queue

IP = socket.gethostbyname(socket.gethostname())
PORT = 5567
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"


Topic_ids = []

def create_topic(conn,addr,Topic_ids):

    ''' = queue.Queue()

    print('Creating New Topic -> ')'''

def handle_admin(conn, addr):
    print('You have a new admin connection')

def send_report(conn,addr):
    print('Sending report to Admin user ->')

def client_request(conn,addr):
    print('sending to client')

def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        
        if msg == DISCONNECT_MSG:
            connected = False
       
        if msg == 'admin':
            handle_admin(conn, addr)

        else: 
            print(f"[{addr}] {msg}")
            

        '''print(msg)'''
        '''print(f"[{addr}] {msg}")'''
        
        
        conn.send(msg.encode(FORMAT)) #server response to client

    conn.close()

def main():
    print("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

if __name__ == "__main__":
    main()