import socket


class Server:
    '''Server handles data streams through sockets.

    Usage Algorithm:

    STEP 1: Create socket to bind to host and port 'localhost:xxxx'
    STEP 2: Listen for client connection
    STEP 3: On connect, call receive data
    STEP 4: Get reply, transmit data
    STEP 5: On quit 'q' close server socket
    '''

    def __init__(self, hostname=socket.gethostname(), port=5000, server_socket=socket.socket()):
        self.hostname = hostname
        self.port = port
        self.server_socket = server_socket

    def on_connection(self):
        connection, address = self.server_socket.accept()
        print("Connection coming in from: " + str(address))
        print('Waiting for message ...\n')

        while True:
            data = connection.recv(1024).decode()
            if not data:
                break
            print("Message from Client: " + str(data))
            data = input('Server: Enter a message > ')
            connection.send(data.encode())

        connection.close()

    def listen(self, number_of_clients):
        '''Bind the hostname and port and listen to a set number of clients.

        :param number_of_clients: max size of allowed clients
        '''
        print('Server listening on:', self.hostname, 'port:', self.port)
        self.bind_hostname_to_port()
        self.listen_to_clients(number_of_clients)

    def bind_hostname_to_port(self):
        '''Bind together the hostname and port'''
        self.server_socket.bind((self.hostname, self.port))

    def listen_to_clients(self, number_of_clients):
        '''Set listening size and listen to clients.

        :param number_of_clients: max size allowed clients
        '''
        self.server_socket.listen(number_of_clients)
