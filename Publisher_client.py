import socket



IP = socket.gethostbyname(socket.gethostname())
PORT = 9994
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"

def main():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")


    Topicname = input("Please Enter a Topic to publish to -> ")
    connected = True
    Topic_ids = 'Topic:' + Topicname
    client.send(Topic_ids.encode(FORMAT))


    
    while connected:
         msg = client.recv(SIZE).decode(FORMAT)

         if 'Yes Topic ->  ' in msg:
             print('')

         if 'No Topic ->  ' in msg:
             print('')
            
         print(f"[SERVER] {msg}")



if __name__ == "__main__":
    main()