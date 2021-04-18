import unittest
from run import app

class ApiTestCases(unittest.TestCase):

    def test_index(self):
        tester = app.test_client(self)
        response = tester.get('/books/v1/get-book-data/?rows=3')
        statuscode = response.status_code
        self.assertEqual(statuscode,200)

    def test_index_content(self):
        tester = app.test_client(self)
        response = tester.get('/books/v1/get-book-data/?rows=3')
        self.assertEqual(response.content_type, 'application/json')

    def test_books_filter_api(self):
        tester = app.test_client(self)
        response = tester.post('/books/v1/get-book-filter-data/',json={"authors":"Bayo Ogunjimi, Abdul Rasheed Na'allah"})
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)
        self.assertEqual(response.content_type, 'application/json')

if __name__ == "__main__":
    unittest.main()
