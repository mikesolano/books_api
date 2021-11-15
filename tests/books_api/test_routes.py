import json
import unittest
import uuid

from app import app


class TestRoutes(unittest.TestCase):

    def setUp(self):
        # setup book data to be used in several tests, reduces code duplication
        self.data = {
            'title': str(uuid.uuid4()),
            'author_first_name': 'Non',
            'author_last_name': 'Grata',
            'year': -1
        }

    def test_get_env(self):
        with app.test_client() as client:
            response = client.get('/api/environment')
            self.assertEqual(200, response.status_code)
            self.assertIn('environment', response.json)
            self.assertEqual('DEV', response.json['environment'])

    def test_create_book(self):
        with app.test_client() as client:
            # create a book
            response = client.post('/api/books',
                                   data=json.dumps(self.data),
                                   content_type='application/json')
            self.assertEqual(201, response.status_code, response.json)
            self.assertIsNotNone(response.json)
            self.assertIn('id', response.json.keys())
            self.assertEqual(self.data['title'], response.json['title'])
            self.assertEqual(self.data['author_first_name'],
                             response.json['author_first_name'])
            self.assertEqual(self.data['author_last_name'],
                             response.json['author_last_name'])
            self.assertEqual(self.data['year'], response.json['year'])

            # attempt to create an invalid book
            self.data.pop('title')
            response = client.post('/api/books',
                                   data=json.dumps(self.data),
                                   content_type='application/json')
            self.assertEqual(400, response.status_code)

    def test_get_books(self):
        with app.test_client() as client:
            response = client.get('/api/books')
            self.assertEqual(200, response.status_code)
            self.assertIsNotNone(response.json)
            self.assertIn('books', response.json)
            self.assertIn('id', response.json['books'][0].keys())

    def test_get_book(self):
        with app.test_client() as client:
            # test for known book
            response = client.get('/api/books/1')
            self.assertEqual(200, response.status_code)
            self.assertIsNotNone(response.json)
            self.assertIn('id', response.json.keys())
            self.assertEqual(1, response.json['id'])

            # test for book that doesn't exist
            response = client.get('api/books/999999999')
            self.assertEqual(400, response.status_code)
            self.assertEqual('Book not found', response.json['message'])

    def test_update_book(self):
        with app.test_client() as client:
            # create a book
            response = client.post('/api/books',
                                   data=json.dumps(self.data),
                                   content_type='application/json')
            self.assertEqual(201, response.status_code, response.json)
            self.assertIn('id', response.json.keys())
            id = response.json['id']
            new_year = response.json['year'] + 1
            reversed_last_name = response.json['author_last_name'][::-1]

            # update book with put
            self.data['year'] = new_year
            print(self.data['year'])
            response = client.put(f'/api/books/{id}',
                                  data=json.dumps(self.data),
                                  content_type='application/json')
            self.assertEqual(200, response.status_code)
            self.assertEqual(new_year, response.json['year'])

            # update book with patch
            patch_data = {'author_last_name': reversed_last_name}
            response = client.patch(f'/api/books/{id}',
                                    data=json.dumps(patch_data),
                                    content_type='application/json')
            self.assertEqual(200, response.status_code)
            self.assertEqual(reversed_last_name,
                             response.json['author_last_name'])

    def test_delete_book(self):
        with app.test_client() as client:
            # create a book
            response = client.post('/api/books',
                                   data=json.dumps(self.data),
                                   content_type='application/json')
            self.assertEqual(201, response.status_code, response.json)
            self.assertIn('id', response.json.keys())
            id = response.json['id']

            # delete book
            response = client.delete(f'/api/books/{id}')
            self.assertEqual(200, response.status_code)

            # check deleted book no long exists
            response = client.get(f'api/books/{id}')
            self.assertEqual(400, response.status_code)
            self.assertEqual('Book not found', response.json['message'])
