import sys
from socket import *
from time import sleep, time
from PyQt5.QtWidgets import *

# Server ile bağlantı
HOST = "localhost"
PORT = 8080

BUFFER_SIZE = 128
ADDR = (HOST,PORT)

CLIENT = socket(AF_INET, SOCK_STREAM)
CLIENT.connect(ADDR)
f = open("client_log.txt","w")

# Arayüz
class win(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()
    def buttonClicked(self):
        # Gönderilen mesaj
        
        first_data = self.lineEditFirstData.text()
        second_data = self.lineEditSecondData.text()
        operation = self.lineEditOperation.text()
        initial_time = time() # Data gönderildiği anda ki saat
        CLIENT.send((first_data+"#"+operation+"#"+second_data).encode())
            
        sleep(0.001) # Sleep fonksiyonunu özellikle ekliyorum localhostta gönderim süresi çok kısa olduğu  
        # için sıfırdan farklı bir değer alabilmek adına bu delayi ekledim.
        get_data = CLIENT.recv(BUFFER_SIZE).decode()
        ending_time = time() # Cevabuın geldiği saat
        elapsed_time = "Gecikme Suresi: "+ str((ending_time-initial_time))+" seconds" # geçen süre RTT

        self.labelGetData.setText(get_data)
        self.labelRTT.setText(elapsed_time)
        if get_data != "Baglanti koptu":
            f.write(get_data+"\n")
            
        if get_data == "Baglanti koptu":
            f.close()

    def initUI(self):
        self.setGeometry(50,50,600,400)
        self.setWindowTitle("Client")
        self.labelInfo = QLabel("Tüm Alanları boş bırakırsanız sunucu-client bağlantısı kopar.", self)
        self.labelInfo.setGeometry(20,20,400,40)
        self.labelGetData = QLabel("Sunucudan Gelen Data", self)
        self.labelGetData.setGeometry(200,120,400,40)
        self.labelRTT = QLabel("Gecikme Süresi", self)
        self.labelRTT.setGeometry(200,170,400,40)  
        self.lineEditFirstData = QLineEdit("İlk Sayı(Zorunlu)",self)
        self.lineEditFirstData.setGeometry(20,70,150,40)
        self.lineEditOperation = QLineEdit("İşlem (+,-,*,/)(Default toplama)",self)
        self.lineEditOperation.setGeometry(20,120,150,40) 
        self.lineEditSecondData = QLineEdit("İkinci Sayı(Zorunlu",self)
        self.lineEditSecondData.setGeometry(20,170,150,40)
        self.pushButtonSend = QPushButton("Hesapla",self)      
        self.pushButtonSend.setGeometry(180,70,150,40)
        self.pushButtonSend.clicked.connect(self.buttonClicked)
        




if __name__ == "__main__":
    app = QApplication(sys.argv) 
    w = win()

    sys.exit(app.exec())       






