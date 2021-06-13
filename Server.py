from socket import *
import threading

HOST = "localhost"
PORT = 8080

BUFFER_SIZE = 128
ADDR = (HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM TCP sunucusu olduğunu gösterir.
SERVER.bind(ADDR)

def calculate(data):
    (first_data, operation, second_data) = data.split("#") 
    result = ""
    if first_data== "":
        first_data = 0
    if second_data == "":
        second_data = 0   
    if operation=="":
        operation = "+"
    if operation == "+":
        result = int(first_data) + int(second_data)
    elif operation == "-":
       result = int(first_data) - int(second_data)
    elif operation == "*":
        result = int(first_data) * int(second_data)
    elif operation == "/":
        result = float(first_data) / float(second_data)
    data = "{} {} {} = {} ".format(first_data,operation,second_data,result)
    return data
      

def handleClient(client):
    status = True
    while status:
        request = client.recv(BUFFER_SIZE).decode()
        print("Gelen veri: "+ request)
        if request != "##":
            data = calculate(request)   
            client.send(data.encode())            
        if request =="##":
            client.send("Baglanti koptu".encode())
            client.close()
            status=False
        
        

while True:
    SERVER.listen(5)
    client, address = SERVER.accept()
    print("%s:%d bağlanti kabul edildi." % (address[0],address[1]))
    clientHandler = threading.Thread(target=handleClient,args=(client,))
    clientHandler.start()    





