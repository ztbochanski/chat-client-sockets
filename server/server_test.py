import unittest
from server import Server


class TestServer(unittest.TestCase):

    """
    Initialization
    """

    def test_instantiation(self):
        """
        A Server exists.
        """
        try:
            Server()
        except NameError:
            self.fail("Could not instantiate Server.")


if __name__ == '__main__':
    unittest.main()
