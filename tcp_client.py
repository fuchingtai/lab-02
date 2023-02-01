"""
Server receiver buffer is char[256]
If correct, the server will send a message back to you saying "I got your message"
Write your socket client code here in python
Establish a socket connection -> send a short message -> get a message back -> ternimate
use python "input->" function, enter a line of a few letters, such as "abcd"
"""
import socket

def main():

    # TODO: Create a socket and connect it to the server at the designated IP and port
    import socket
    
    HOST = '192.168.1.26' # Standard loopback interface address (localhost)
    PORT = 8000   # Port to listen on (non-privileged ports are > 1023)
    
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    	
    	s.connect((HOST,PORT)) #.connect to connect to server
    				#socket type. AF_INET is the Internet address family for IPv4
    				#SOCK_STREAM is the socket type for TCP
    
    # TODO: Get user input and send it to the server using your TCP socket
    	user_input = input("Please enter input: ") #write a message before the input
    	s.sendall(user_input.encode())             #s.sendall() to send message
    	
    # TODO: Receive a response from the server and close the TCP connection
    	data = s.recv(256)              #server receiver buffer is char[256]
    	output = data.decode()
    	print("Received: " + output) #print recieved message
    	s.close()                       #close TCP connection
    	


if __name__ == '__main__':
    main()
