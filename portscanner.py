import socket

ports = input("Enter range of ports 1-1000: ")
# 1-1000

start,end = ports.split('-')

start=int(start) 
end = int(end)
for i in range(start,end+1 ):

    try:
        s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        s.connect(('192.168.1.1',i))

        print("port {} is open".format(i))
        s.close()

    except:
        pass
        #print("port {} is closed".format(i))