import requests
import unittest

from flask.ext.testing import LiveServerTestCase

from MicroMote import create_app
from MicroMote.config import TestingConfig


class TestCase(LiveServerTestCase):
    """ The base test case """

    def create_app(self):
        app = create_app(config=TestingConfig)
        return app

    def test_server_is_up_and_running(self):
        response = requests.get(self.get_server_url())
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
