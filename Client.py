from socket import *
from time import sleep, time

# Server ile bağlantı
HOST = "localhost"
PORT = 8080

BUFFER_SIZE = 128
ADDR = (HOST,PORT)

CLIENT = socket(AF_INET, SOCK_STREAM)
CLIENT.connect(ADDR)
f = open("Client_Log.txt","w")
print("Çıkış yapmak için bütün alanları boş bırakmanız gerekmektedir!")
# Gönderilen mesaj
while True:
   
    first_data = input("İlk sayıyı giriniz: ")
    second_data = input("İkinci sayıyı giriniz: ")
    operation = input("Yapılacak işlemin sembolünü giriniz(+,-,*,/): ")
    initial_time = time()
    CLIENT.send((first_data+"#"+operation+"#"+second_data).encode())
    
    sleep(0.001) # Sleep fonksiyonunu özellikle ekliyorum localhostta gönderim süresi çok kısa olduğu için sıfırdan farklı bir değer alabilmek adına bu delayi ekledim.
    
    get_data = CLIENT.recv(BUFFER_SIZE).decode()
    ending_time = time()
    elapsed_time = "Gecikme Suresi: "+ str((ending_time-initial_time))+" seconds"

    print(get_data)
    print(elapsed_time)
    if get_data != "Baglanti koptu":
        f.write(get_data+"\n")
    
    if get_data == "Baglanti koptu":
        f.close()
        break

