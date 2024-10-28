import unittest
from app.hello_world_server import app
class TestHelloWorldServer(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True
    def test_hello_world_route(self):
        """Test the root route returns 'Hello, World!' with status code 200"""
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello, World!')
if __name__ == '__main__':
    unittest.main()