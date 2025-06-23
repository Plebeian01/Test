import unittest
import subprocess

class TestHello(unittest.TestCase):
    def test_hello_world_output(self):
        process = subprocess.run(['python', 'hello.py'], capture_output=True, text=True)
        self.assertEqual(process.stdout.strip(), "Hello, World!")

if __name__ == '__main__':
    unittest.main()
