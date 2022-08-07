
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

    def __init__(self, hostname=socket.gethostname(), port='5000', socket=socket.socket()):
        self.hostname = hostname
        self.port = port
        self.socket = socket
