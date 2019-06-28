import unittest
import sys
# Add all test cases from all test classes like the line below.

if __name__ == '__main__':

    if sys.argv[1] == 'init':
        from tests.InitTest import TestRunning
    unittest.main()

