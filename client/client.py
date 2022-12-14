import socket


class Client:
    '''Client transmits and receives data through sockets.

    Usage Algorithm:

    STEP 1: Create socket and connect to host: ex. 'localhost:xxxx'
    STEP 2: On connection, get input to send
    STEP 3: If message is quit exit client, close socket
    STEP 4: Else, transmit data
    STEP 5: Receive any data
    STEP 6: Display data
    '''

    def __init__(self, server_name=socket.gethostname(), server_port=5000, client_socket=socket.socket()):
        self.server_name = server_name
        self.server_port = server_port
        self.client_socket = client_socket

    def on_connection(self):
        print('/q to quit')
        print('Enter message to send...\n')

        user_input = self.get_input()

        while user_input.lower().strip() != '/q':
            self.client_socket.send(user_input.encode())
            data = self.client_socket.recv(1024).decode()
            print('Message from server:', data)
            user_input = self.get_input()

        self.client_socket.close()

    def connect_to_server(self):
        '''Connect to the server.'''
        self.client_socket.connect((self.server_name, self.server_port))

    def get_input(self):
        '''Get user input.

        :return: String
        '''
        message = input('Client: Enter a message > ')
        return message
