import socket

target_host = "www.test.com"
target_port = 8080

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# send some data
client = socket.sendto(b"AAABBBCCC", (target_host, target_port))

# receive some data
data, addr = client.recvfrom(4096)

# print the response
print(response.decode())

# close the connection
client.close()
