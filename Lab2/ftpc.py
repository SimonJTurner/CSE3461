# Echo client program
import socket

HOST = 'gamma'    # The remote host
PORT = 5000              # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

filename = str(sys.argv[3])
file = open(filename, 'rb')

chunksize = 1024
while True:
	data = file.read(chunksize)
	if data:
		s.sendall(data)
	else:
		break

data = s.recv(1024)
s.close()
print ('Received', repr(data))


