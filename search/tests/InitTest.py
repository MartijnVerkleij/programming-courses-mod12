import unittest
from pacman import runGames, readCommand


class TestRunning(unittest.TestCase):

    def setUp(self):
        pass
        
    def test_running(self):
        try:
            args = readCommand(['-l', 'testMaze', '--pacman', 'GoWestAgent'])
            runGames(**args)
        except Exception as e:
            self.fail('The test environment was not set up correctly: \n{}'.format(e.message))


def run():
    unittest.main()


if __name__ == '__main__':
    run()

