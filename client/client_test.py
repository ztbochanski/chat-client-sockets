import unittest
from client import Client


class TestClient(unittest.TestCase):

    def test_instantiation(self):
        '''
        A Client exists.
        '''
        try:
            Client()
        except NameError:
            self.fail('Could not instantiate Client.')

    def test_hostname(self):
        '''
        A Client connects to a hostname.
        '''
        self.assertIsNotNone(Client().server_name)

    def test_port(self):
        '''
        A Client has a port.
        '''
        client = Client()
        self.assertEqual(5000, client.server_port)
        self.assertIsNotNone(client.server_port)


if __name__ == '__main__':
    unittest.main()
