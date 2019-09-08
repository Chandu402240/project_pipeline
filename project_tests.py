#!/usr/bin/env python

import unittest
import project_app

class TestHello(unittest.TestCase):

    def setUp(self):
        project_app.app.testing = True
        self.app = project_app.app.test_client()

    def test_hello(self):
        rv = self.app.get('/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World! This is Project v0.1 Dockerizing Jenkins Pipeline\n')

    def test_hello_hello(self):
        rv = self.app.get('/hello/')
        self.assertEqual(rv.status, '200 OK')
        self.assertEqual(rv.data, b'Hello World! This is Project v0.1 Dockerizing Jenkins Pipeline\n')

    def test_hello_name(self):
        #name = 'test'
        rv = self.app.get('/hello/test')
        self.assertEqual(rv.status, '200 OK')


if __name__ == '__main__':
    unittest.main()
