import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('whois.internic.net', 43))
s.send(b"sina.com.cn \r\n")
response =b''
while True:
    data = s.recv(4096)
    response += data
    if not data :
        break
s.close()
print(response.decode())
