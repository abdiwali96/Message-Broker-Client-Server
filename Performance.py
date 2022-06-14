from curses import window
import tkinter as tk # Python 3 import
# import Tkinter as tk # Python 2 import
import socket

root = tk.Tk()
def tick():
    global sec
    if not doTick:
        return
    sec += 0.1
    sec = round(sec,1)
    timeLabel.configure(text=sec)
    root.after(100, tick)

def stop():
    global doTick
    doTick = False

def start():
    global doTick
    doTick = True
    # Perhaps reset `sec` too?
    tick()

sec = 0
doTick = True

def my_function():

    start()

    current_id = my_entry.get()
    url_member = str(current_id)

    msg100_json = '{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},{"test":"message"},'



            
    msg100 = str(msg100_json)  
    print(msg100) 
    print(url_member)   #this will be the topic

    IP = socket.gethostbyname(socket.gethostname())
    PORT = 9996
    ADDR = (IP, PORT)
    SIZE = 1024
    FORMAT = "utf-8"
    DISCONNECT_MSG = "!DISCONNECT"


    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client connected to server at {IP}:{PORT}")


    Topicname = url_member
    connected = True
    Topic_ids = 'Topic:' + Topicname
    client.send(Topic_ids.encode(FORMAT))


    
    
    msg = client.recv(SIZE).decode(FORMAT)

    if 'Yes Topic' in msg:
        print('\nTopic group already exist..')
        

        splitmsg = msg.split(",")
        print(splitmsg)
        #splitting message to grab Topic name
        topicname = splitmsg[1]

        
        messageinput = msg100
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
    stop()


    repeat = input('WOULD YOU LIKE TO REPEAT TEST')



    

my_label = tk.Label(root, text = "Enter Topic name to Publish to ",font=("Helvetica", 25))
my_label.place(x= 150, y = 100)
root.title('Welcoem to Performance testing')
root.geometry("600x300+10+20")
my_entry = tk.Entry(root)
my_entry.place(x= 200, y = 150)

my_button = tk.Button(root, text = "START", command = my_function)
my_button.place(x= 400, y = 150)


my_label3 = tk.Label(root, text = "TIMER -> ",font=("Helvetica", 15))
my_label3.place(x= 150, y = 200)

timeLabel = tk.Label(root, fg='green',font=('Helvetica',15))
timeLabel.place(x= 250, y = 200)






root.mainloop()




