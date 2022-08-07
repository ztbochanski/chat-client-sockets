import unittest
from server import Server
import socket


class TestServer(unittest.TestCase):

    def test_instantiation(self):
        '''
        A Server exists.
        '''
        try:
            Server()
        except NameError:
            self.fail('Could not instantiate Server.')

    def test_hostname(self):
        '''
        A server has a hostname.
        '''
        self.assertIsNotNone(Server().hostname)

    def test_port(self):
        '''
        A server has a port.
        '''
        self.assertIsNotNone(Server().port)

    def test_socket(self):
        '''
        A server has a socket.
        '''
        self.assertIsNotNone(Server().socket)


if __name__ == '__main__':
    unittest.main()
