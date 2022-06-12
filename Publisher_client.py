import socket



IP = socket.gethostbyname(socket.gethostname())
PORT = 9996
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

         if 'Yes Topic' in msg:
             print('\nTopic group already exist..')
             while connected:

                splitmsg = msg.split(",")
                print(splitmsg)
                #splitting message to grab Topic name
                topicname = splitmsg[1]

                
                messageinput = input("\nWhat message would you like send to this Topic -> ")
                send_message = topicname +  '#' + ' MESSAGE#' +  messageinput

               
                client.send(send_message.encode(FORMAT))


         if 'No Topic' in msg:

             print('\nTopic group does not Exist')

             splitmsg = msg.split(",")
             print(splitmsg)
             #splitting message to grab Topic name
             topicname = splitmsg[1]

             
             topicinput = input("\nPlease a new phrase for a Topic-> ")
             create_topic = topicname + '#' + ' CREATE#' +  topicinput
             client.send(create_topic.encode(FORMAT))
            
         print(f"[SERVER] {msg}")



if __name__ == "__main__":
    main()