import socket
import os

class SimpleHTTPServer:
    def __init__(self, host='127.0.0.1', port=8080):
        self.host = host
        self.port = port
        #Creating a TCP socket and using IPV4
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Allow immediate reusage of the port after stopping the server
        self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
    def start(self):
        """Start this server and listen to some shit messages and pornhub ahh"""
        self.server_socket.bind((self.host, self.port)) # bind the socket to the ip address and port
        self.server_socket.listen(5) # put the server on listen and mod and allow 5 connections at maximum before refusing them
        print(f"Server running on the fucking http://{self.host}:{self.port}")
        
        try:
            while True:
                #Wait for a client connection via the fucking browser
                client_socket, client address = self.server_socket.accept() #usage of the specified port in the computer and returning a client socket
                print(f"Connection received from {client_address}") #yeey connection received
                self.handle_client(client_socket)
        except KeyboardInterrupt:
            print("\nshutting down the server gracefully...")
        finally:
            self.server_socket.close()
        
    def handle_client(self, client_socket):
        """Processes the client request and sends back an HTTP response."""
        try:
            #Receive data from the client (usually up to 1024 bytes is enough for headers) and decoding the fucking raw bits
            request_data = client_socket.recv(1024).decode('utf-8')
            if not request_data:
                client_socket.close()
                return
            
            # Parse the first line of the HTTP request (e.g., "GET /index.html HTTP/1.1")
            request_lines = request_data.split("\r\n")
            first_line = request_lines[0]
            parts = first_line.split(" ") #split the first line into parts because you are gay <_<
            
            if len(parts) >= 2:
                method = parts[0] #sp the method supposedly GET is gonna be on the first index
                filename = parts[1]# and the fucking filename demanded by the client is on the second index
            else:
                method = ""
                filename = ""
            
            #Only handle GET requests for simplicity
            if method == "GET":
                self.serve_file(client_socket, filename) #return a client socket with the file demanded
            else:
                self.send_error(client_socket, 405, "Method Not Allowed") #Send an error with the number 405 and a message
            
        except Exception as e:
            print("Error handling request: {e}")
        finally:
            client_socket.close()
            
            
            
            