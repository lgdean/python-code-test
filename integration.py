import unittest
from program import *

class TestWholeProgram(unittest.TestCase):
    def test_output(self):
        f = open("model_output.txt","r")
        expected = f.readlines()
        f.close()
        # TODO want to pass file names in at some point
        prog = Program()
        actual = prog.doit()
        for idx, line in enumerate(expected):
            self.assertEqual(line.rstrip(), actual[idx])
        return

if __name__ == '__main__':
    unittest.main()
