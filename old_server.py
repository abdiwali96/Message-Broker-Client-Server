from audioop import add
import socket
import threading
import queue
import json
from grpc import server
import json

import mysql.connector

IP = socket.gethostbyname(socket.gethostname())
PORT = 9994 #using 9999 as the welcome port number
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
    print(addr[0])#IP Add

    #adding topic to Json record
    filename = 'Messages.json'
    entry = {"Topicname": Topic_ID, "Port": "0000", "IP": "00:00:00"}

    # 1. Read file contents
    with open(filename, "r") as file:
        data = json.load(file)
    # 2. Update json object
    data.append(entry)
    # 3. Write json file
    with open(filename, "w") as file:
        json.dump(data, file)

    
    #Step 3: creating Queue with the new topic name
   
    
   


    try: 
         #Step 4:try top add topic name to the array of topic Ids
    # Topic_ids_list.append('g')
     #print('Created a New Topic Queue: -> ' +  str(Topic_ID))

    # conn.send('Created a New Topic Queue: -> ' +  Topic_ID.encode(FORMAT))



     '''Parse Json now'''
    except:
        print('flop')

 

def checkTopicExist(Topic_ids_list):

 print('')

def addToQueue(conn,addr,JsonMsg):

    print('addToQueue')

def handle_admin(conn, addr):
    print('You have a new admin connection')

def send_report(conn,addr):
    print('Sending report to Admin user ->')

def client_request(conn,addr):
    print('sending to client')

def check_group_exist(conn,addr,msg,mydb):

    # Split message to get the group name
    splitgroup = msg.split(":")
    #print(splitgroup)
   # will use group name in SQL query
    groupname = splitgroup[1]



    sql_select_Query = "select * from Groups where Group_Name='%s'" % (groupname)
    cursor = mydb.cursor()
    cursor.execute(sql_select_Query)

    myresult = cursor.fetchall()

    

    print('\n...SEARCHING DB FOR GROUP -> ' + groupname + ' ....\n')
      
    if cursor.rowcount==1:
        print('Group ' + groupname + ' does exist')
        ## Do your thing here
       
        # now will send a confirmation to client that group exist

    else:
         print('Group ' + groupname + ' does NOT exist')
    
   
def check_Topic_exist(conn,addr,msg,mydb):

    # Split message to get the Topic name
    splitTopic = msg.split(":")
   
   # will use group name in SQL query
    Topicname = splitTopic[1]



    sql_select_Query_topic = "select * from messages where Topic_name='%s'" % (Topicname)
    cursor1 = mydb.cursor()
    cursor1.execute(sql_select_Query_topic)

    myresult = cursor1.fetchall()

    print('\n...SEARCHING DB FOR TOPIC -> ' + Topicname + ' ....\n')

    if cursor1.rowcount==1:
        print('\nTopic Response,' + Topicname + ', does exist')
        foundtopic = 'Yes Topic,' + Topicname + ', does exist'
        conn.send(foundtopic.encode(FORMAT))
       
        
        # now will send a confirmation to client that Topic exist

    else:
        print('\nTopic Response,' + Topicname + ', does NOT exist')
        Notfoundtopic = 'No Topic,' + Topicname + ', does NOT exist'
        conn.send(Notfoundtopic.encode(FORMAT))

def DB_Message_input(topicname,clientmessage,mydb): #This function will find the record in db and add the message
    print('')

    # BEFORE UPDATING RECORD BE NEED FIRST GET THE EXISTING RECORD BEFORE ADDING TO IT
    mycursor = mydb.cursor()
    sql = "SELECT message_values FROM messages WHERE Topic_name ='%s'" % (topicname)
    mycursor.execute(sql)
    

    result = mycursor.fetchone()
    new = str(result[0]) + ',' + clientmessage  # This is the new message that is to be updated to DB

    print(new)


    sql2 = "UPDATE messages SET message_values = '%s' WHERE Topic_name = '%s'" % (new, topicname)
    mycursor2 = mydb.cursor()
    mycursor2.execute(sql2)

    mydb.commit()

    print(mycursor2.rowcount, "record(s) affected")

def Create_Topic_DB(clienttopic,mydb):

    mycursor = mydb.cursor()

    sql = "INSERT INTO messages (Topic_name,message_values) VALUES (%s,%s)"
    val = (clienttopic,'')
    mycursor.execute(sql, val)

    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    print('')

def handle_client(conn, addr,mydb):
    print(f"[NEW CONNECTION] {addr} connected.")


    connected = True
    while connected:
        msg = conn.recv(SIZE).decode(FORMAT)
        
        if msg == DISCONNECT_MSG:
            connected = False
       
        if msg == 'admin':
            handle_admin(conn, addr)

        if 'Group:' in msg:
            print('your topic name is ' + msg) 
            # server will check if the group has already been created in the database
            check_group_exist(conn,addr,msg,mydb)


        if 'Topic:' in msg:
           
            # server will check if the Topic has already been created in the database
            check_Topic_exist(conn,addr,msg,mydb)

        if 'CREATE' in msg:
             splitmsg = msg.split("#")
             print(splitmsg)
             #splitting message to grab Topic name
             topicname = splitmsg[0]  #topic
             clienttopic = splitmsg[2] # client message part
            #will now need to parse the JSON
             Create_Topic_DB(clienttopic,mydb)

             success = 'Yes Topic created,' + clienttopic
             conn.send(success.encode(FORMAT))




        if 'MESSAGE#' in msg:
             splitmsg = msg.split("#")
             print(splitmsg)
             #splitting message to grab Topic name
             topicname = splitmsg[0]  #topic
             clientmessage = splitmsg[2] # client message part
            #will now need to parse the JSON

             print(clientmessage)
             data = json.loads(str(clientmessage))

             final_message = ''
             for message in data:
                  print(data[message])
                  final_message+=data[message] + ','
                  

             print(final_message)  
             final_message = final_message[:-1] 
             DB_Message_input(topicname,final_message,mydb)
             print('')


              #Now call function to add to database.




        # if 'Topic' in msg:
            
        #     if isinstance(msg, str): 
        #      print('YES ITS A STRING' + msg)
        # # check if topic already exist
        # # if no then create topic
        #      create_topic(conn,addr,msg,Topic_ids_list )
        #      Topic_ID = queue.Queue()
        #      Topic_ID.put('helakka')
        #      print(Topic_ID.get())

        #      print(Topic_ID.qsize()) 

        #     else:
        #         print('NO its not a string ' + msg)


       


        # if 'MESSAGE' in msg:
        #     print('receveied message ' + msg)
        #     Topic_ID.put('TESTING')
        #     print(Topic_ID.get())
        #     print(Topic_ID.qsize()) 

            
           

        #      # ADD TO AN MSG to an existing queue (NOTE, the first part of the message make it have the topic name so you know)
            
        # else: 
        #     print(f"[{addr}] {msg}")
            

        # '''print(msg)'''
        # '''print(f"[{addr}] {msg}")'''
        
        
       # conn.send(msg.encode(FORMAT)) #server response to client

    conn.close()

def main():
    
     #MYSQL DATABASE CONNECt
    mydb = mysql.connector.connect(
    host="localhost",
    database='MessageBroker',
    user="root",
    password=""
    )


    print("Server is starting Up...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
   
    print(f"Server is now LISTENING on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr, mydb))
        thread.start()
        print(f"[ACTIVE CONNECTIONS] {threading.activeCount() - 1}")

        

if __name__ == "__main__":
    main()