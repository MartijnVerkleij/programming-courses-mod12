import unittest
import sys
# Add all test cases from all test classes like the line below.



if __name__ == '__main__':

    if 'init' in sys.argv:
        from tests.InitTest import TestRunning
        sys.argv.remove('init')
        
    if 'eightpuzzle' in sys.argv:
        from tests.InitTest import TestRunning
        sys.argv.remove('eightpuzzle')
    unittest.main()

