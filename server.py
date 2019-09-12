import socket
import sys

def socket_create():
    try:
        global port
        global host
        global s

        port=9999
        host=''
        s=socket.socket()
    except :
        print('Error in Socket creation' + str(socket.error))
def socket_binding():
    try:
        global port
        global host
        global s
        print('Binding the port : ' + str(port))
        s.bind((host,port))
        s.listen(5)
    except:
        print('Socket binding error:' + str(socket.error) + '\n' +'retrying...')
        
def accept_socket():
    conn,address=s.accept()
    print('Connection has been established. |  IP' + address[0] + '|' + 'Port' + str(address[1]))
    send_commands(conn)
    conn.close()
def send_commands(conn):
    while True:
        cmd=input()
        if cmd == 'exit':
            s.close()
            conn.close()
            sys.exit()
        if len(str.encode(cmd))>0:
            conn.send(str.encode(cmd))
            client_response=str(conn.recv(1024),'utf-8')#1024 is basically recieving chunks of bits of size 1024.the connection sent or recieve cannot be string hence encoding to bits format is done.
            print(client_response,end='')
def main():
    socket_create()
    socket_binding()
    accept_socket()
main()    
