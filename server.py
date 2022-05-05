import socket
import threading
import queue
from tkinter import E

IP = socket.gethostbyname(socket.gethostname())
PORT = 5567
ADDR = (IP, PORT)
SIZE = 1024
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"



Topic_ids_list  = []

def create_topic(conn,addr,Topic_ids,Topic_ids_list ):

   
    #Step 1: split the client input to select topic name
    splitTopic = Topic_ids.split(":")
    print(splitTopic)
    #Step 2: assigning second element as the official new name
    Topic_ID = splitTopic[1]
    print(Topic_ID)
    #Step 3: creating Queue with the new topic name
    Topic_ID = queue.Queue()

    print(Topic_ID.qsize())
    
   

    print('we here')

    try: 
         #Step 4:try top add topic name to the array of topic Ids
    # Topic_ids_list.append('g')
     #print('Created a New Topic Queue: -> ' +  str(Topic_ID))

    # conn.send('Created a New Topic Queue: -> ' +  Topic_ID.encode(FORMAT))



     '''Parse Json now'''
    except:
        print('flop')

 

def checkTopicExist(Topic_ids_list):

    if ('4' in Topic_ids_list):
        print ("Topic Exists")

    else:
        print('Requesting')


def addToQueue(conn,addr,JsonMsg):

    print('addToQueue')


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

        if 'Topic' in msg:
            
            if isinstance(msg, str): 
             print('YES ITS A STRING' + msg)
             create_topic(conn,addr,msg,Topic_ids_list )

            else:
                print('NO its not a string ' + msg)
            

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