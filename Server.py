from socket import *
import threading

HOST = "localhost"
PORT = 8080

BUFFER_SIZE = 128
ADDR = (HOST,PORT)

SERVER = socket(AF_INET, SOCK_STREAM) # SOCK_STREAM TCP sunucusu olduğunu gösterir.
SERVER.bind(ADDR)

def calculate(data):
    (first, operation, second) = data.split("#")
    result = ""
    if first== "":
        first = 0
    if second == "":
        second = 0   
    if second== "0" and first == "0" and operation=="/":
        return "0 / 0 = BOLUNEMEZ "      

    if operation == "+":
        result = int(first) + int(second)
    elif operation == "-":
        result = int(first) - int(second)
    elif operation == "*":
        result = int(first) * int(second)
    elif operation == "/":
        result = float(first) / float(second)
    elif operation!="+" or operation!="-" or operation!="*" or operation!="/" or operation=="":
        return "Tanimsiz islem! "    
    data = "{} {} {} = {} ".format(first,operation,second,result)
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





