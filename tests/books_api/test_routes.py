import json
import unittest
import uuid

from app import app


class TestRoutes(unittest.TestCase):

    def test_get_env(self):
        with app.test_client() as client:
            response = client.get('/api/environment')
            self.assertEqual(response.status_code, 200)
            self.assertIn('environment', response.json)
            self.assertEqual(response.json['environment'], 'DEV')

    def test_get_books(self):
        with app.test_client() as client:
            response = client.get('/api/books')
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.json)
            self.assertIn('books', response.json)
            self.assertIn('id', response.json['books'][0].keys())

    def test_get_book(self):
        with app.test_client() as client:

            # test for known book
            response = client.get('/api/books/1')
            self.assertEqual(response.status_code, 200)
            self.assertIsNotNone(response.json)
            self.assertIn('id', response.json.keys())
            self.assertEqual(response.json['id'], 1)
            self.assertEqual(response.json['title'], 'Dune')

            # test for book that doesn't exist
            response = client.get('api/books/999999999')
            self.assertEqual(response.status_code, 400)
            self.assertEqual(response.json['message'], 'Book not found')

    def test_create_book(self):
        with app.test_client() as client:

            title = str(uuid.uuid4())
            data = {
                'title': title,
                'author_first_name': 'Non',
                'author_last_name': 'Grata',
                'year': -1
            }

            # create a book
            response = client.post('/api/books',
                                   data=json.dumps(data),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 201, response.json)
            self.assertIsNotNone(response.json)
            self.assertIn('id', response.json.keys())
            self.assertEqual(response.json['title'], title)
            self.assertEqual(response.json['author_first_name'], 'Non')
            self.assertEqual(response.json['author_last_name'], 'Grata')
            self.assertEqual(response.json['year'], -1)

            # attempt to create an invalid book
            data['title'] = None
            response = client.post('/api/books',
                                   data=json.dumps(data),
                                   content_type='application/json')
            self.assertEqual(response.status_code, 400)
