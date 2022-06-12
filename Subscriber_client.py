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


    Groupname = input("Please Enter a group name-> ")
    connected = True
    group_ids = 'Group:' + Groupname
    client.send(group_ids.encode(FORMAT))


    
    while connected:
         msg = client.recv(SIZE).decode(FORMAT)

        
         if 'group results#' in msg:

            
            original_string = msg

            characters_to_remove = "[]()']"


            new_string = original_string

            for character in characters_to_remove:

             new_string = new_string.replace(character, "")


            strippedString = str(msg).strip(",")

                  
            print('\nPlease enter the POSITION NUMBER of the group your like to retrieve na update from')
            print('OR type the word CREATE NEW, to subscribe to a new topic\n')
            splitmsg = new_string.split("#",1)[1]
            
            #splitting message to grab Topic name
            
            
            splitmsg2 = splitmsg.split(",")
            #print(splitmsg2)
            #splitting message to grab Topic name
            

           # print(len(splitmsg2))
            for x in splitmsg2[:-1]:
                print('  -: ' + x)
            
            print(splitmsg2[0])

            topic_name_update = int(input("\nPlease Enter Topic name you would like to get message update -> "))
           
            Update_msg = 'UPDATE#' + splitmsg2[topic_name_update-1] + '#' + msg
            client.send(Update_msg.encode(FORMAT))


         if 'NOT EXISIT#' in msg:
             user_input = input('[SERVER] GROUP DOES NOT EXIST..Would you like to create a new group ->')

             if(user_input == 'yes'):
                 input('PLEASE ENTER NEW GROUP -> ')

         if 'COMPLETED' in msg:
             print('[SERVER] - RECORD HAS BEEN UPDATED')

         print(f"[SERVER] {msg}")



if __name__ == "__main__":
    main()