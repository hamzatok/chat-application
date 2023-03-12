
import socket
import time

host = "localhost"
port = 7777

s = socket.socket()
s.bind((host,port))

s.listen(1)

baglanti, adres = s.accept()
print(str(adres), "bağlantı sağlandı")

while True:
    while True:
        try:
            gelen_veri = str(baglanti.recv(1024).decode())
            print("CLIENT: ", gelen_veri)
            break
        except ConnectionResetError:
            time.sleep(2)
            baglanti, adres = s.accept()
            print(str(adres)+ " bağlantı sağlandı.")

    if gelen_veri=="cikis":
        break
    else: 
        mesaj = input("SERVER: ")
        print("client bekleniyor...")
        baglanti.send(mesaj.encode())

baglanti.close()
            
