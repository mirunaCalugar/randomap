from app import app
import unittest

class BasicTestCase(unittest.TestCase):

    def test_home(self):
        """Test the home page loads correctly."""
        # Create a test 
        tester = app.test_client(self)

       
        response = tester.get('/', content_type='html/text')

       
        self.assertEqual(response.status_code, 200)

       
        self.assertIn(b'Random Earth Teleporter', response.data)

if __name__ == '__main__':
    unittest.main()