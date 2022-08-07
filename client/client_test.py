import unittest
from client import Client
import socket


class TestClient(unittest.TestCase):

    def test_instantiation(self):
        '''
        A Client exists.
        '''
        try:
            Client()
        except NameError:
            self.fail('Could not instantiate Client.')


if __name__ == '__main__':
    unittest.main()
