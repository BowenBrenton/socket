import socket

target_host = "www.test.com"
target_port = 8080

# create a socket object AFINTET FOR IPV4, SOCK STREAM IS FOR TCP
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# connecting to the client by pulling in variable for the host and the port
client.connect((target_host, target_port))

# get request for http with host. What are the r & n for?
client.send(b"GET / HTTP/1.1\r\nHost: www.test.com\r\n\r\n")

# receive the data from the server what is the 4096 for?
response = client.recv(4096)

# print the response
print(response.decode())

# close the connection
client.close()