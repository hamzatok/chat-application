import socket
import time

host = "localhost"
port = 7777

s = socket.socket()
s.connect((host,port))



print("bağlantı sağlandı -> {host}:{port}")


mesaj = input("CLIENT: ")
print("server bekleniyor...")
        
while mesaj != "cikis":
    s.send(mesaj.encode())
    gelen_veri = s.recv(1024).decode()
    print("SERVER: ", gelen_veri)

    mesaj = input("CLIENT: ")
    print("server bekleniyor...")

s.close()